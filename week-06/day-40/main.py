from datetime import date

print("Welcome to Birthday Reminder CLI!")

person_name = input("Enter name: ").strip()
birthday_text = input("Enter birthday (YYYY-MM-DD): ").strip()
birthday_date = date.fromisoformat(birthday_text)

today = date.today()
next_birthday = birthday_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days

print(f"{person_name}'s next birthday is in {days_left} day(s).")
