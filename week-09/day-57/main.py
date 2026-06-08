from datetime import date

print("Welcome to Birthday Email Draft Generator!")

friend_name = input("Enter friend's name: ").strip()
sender_name = input("Enter your name: ").strip()

subject = f"Happy Birthday, {friend_name}!"
body = (
    f"Dear {friend_name},\n\n"
    "Wishing you a wonderful birthday filled with joy and success.\n"
    f"Have a great day!\n\n"
    f"Best wishes,\n{sender_name}\n"
    f"Draft date: {date.today().isoformat()}"
)

print("\nSubject:")
print(subject)
print("\nBody:")
print(body)
