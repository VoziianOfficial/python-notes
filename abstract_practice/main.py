from notifications import Notification, EmailNotification


email = EmailNotification("yuliia@example.com", "Hello!")


email.show_info()
email.send()


