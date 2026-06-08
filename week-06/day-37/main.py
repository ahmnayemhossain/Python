class ValidationError(Exception):
    pass


def validate_name(name):
    if len(name.strip()) < 3:
        raise ValidationError("Name must be at least 3 characters long.")


def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValidationError("Email format is invalid.")


def validate_age(age_text):
    age = int(age_text)
    if age < 18:
        raise ValidationError("Age must be at least 18.")
    return age


print("Welcome to Form Validator CLI!")

try:
    name = input("Enter name: ")
    email = input("Enter email: ")
    age_text = input("Enter age: ")

    validate_name(name)
    validate_email(email)
    age = validate_age(age_text)
except ValueError:
    print("Age must be a number.")
except ValidationError as error:
    print(f"Validation error: {error}")
else:
    print(f"Valid form submitted for {name}, {email}, age {age}.")
