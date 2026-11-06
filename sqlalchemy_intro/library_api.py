from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///sqlalchemy_intro/sqlalchemy.db")


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")



class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship(back_populates="books")



Base.metadata.create_all(engine)


class AuthorCreate(BaseModel):
    name: str


class BookCreate(BaseModel):
    title: str
    author_id: int


app = FastAPI()


@app.post("/authors", status_code=201)
def create_author(author: AuthorCreate):
    with Session(engine) as session:
        new_author = Author(name=author.name)

        session.add(new_author)
        session.commit()

        return {
            "id": new_author.id, 
            "name": new_author.name
            }


@app.get("/authors")
def get_authors():

    with Session(engine) as session:
        statement = select(Author)

        authors = session.scalars(statement).all()

        result = []

        for author in authors:
            result.append(
                {
                    "id": author.id,
                    "name": author.name,
                }
            )

        return result



@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    with Session(engine) as session:
        statement = select(Author).where(Author.id == book.author_id)
        author = session.scalar(statement)

        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        
        new_book = Book(
            title=book.title, 
            author_id=book.author_id)

        session.add(new_book)
        session.commit()

        return {
            "id": new_book.id,
            "title": new_book.title,
            "author_id": new_book.author_id,
        }



@app.get("/authors/{author_id}/books")
def get_books_by_author(author_id: int):
    with Session(engine) as session:
        statement = select(Author).where(Author.id == author_id)
        author = session.scalar(statement)

        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")

        result = []

        for book in author.books:
            result.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author_id": book.author_id,
                }
            )

        return result   