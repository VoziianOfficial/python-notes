from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def show_info(self):
        print(f"Recipient: {self.recipient}")
        print(f"Message: {self.message}")

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def __init__(self, recipient, message):
        super().__init__(recipient, message)

    def send(self):
        print(f"Email sent to {self.recipient}: {self.message}")


