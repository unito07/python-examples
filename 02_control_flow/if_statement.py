# If Statements and Control Flow

# Get user's age
age = int(input("Enter your age: "))

# Check age and print appropriate message
if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 30:
    print("You're in your twenties")
elif age < 40:
    print("You're in your thirties")
else:
    print("You're over 40")

# Simple grade checker
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")