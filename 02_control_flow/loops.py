# Examples of Loops in Python

# For loop with a list
print("For loop with a list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}s")

# For loop with range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# While loop
print("\nWhile loop countdown:")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")

# Break and continue
print("\nNumbers from 1 to 10 (skipping 5):")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    print(i)
    if i == 8:
        break  # Stop at 8