from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


password = "123456"

hashed_password = password_hash.hash(password)

print("Password:", password)
print("Hash:", hashed_password)


is_correct = password_hash.verify("4533221", hashed_password)

print(is_correct)
