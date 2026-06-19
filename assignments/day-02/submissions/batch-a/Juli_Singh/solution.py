# Question 1: Positive, Negative, or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Question 2: Even or Odd

number = int(input("Enter another number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 3: Print list using loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)


# Question 4: Function to calculate average

def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

avg = calculate_average(80, 90, 85)
print("Average:", avg)


# Question 5: Function to grade student

def grade_student(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Grade F")

grade_student(85)