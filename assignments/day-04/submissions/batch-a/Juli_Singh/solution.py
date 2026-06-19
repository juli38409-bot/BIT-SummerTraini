
students = ["Aman", "Priya", "Shalu", "Raj", "Ansh"]
students.append("Vivek")
print(students)

cities = ("Mumbai", "Kanpur", "Delhi", "Lucknow", "Agra")
print(cities[2])

courses = {"Python", "SQL", "Machine Learning", "Data Analytics"}
courses.add("AI")
print(sorted(courses))

student = {
    "name": "Rahul",
    "course": "Python Data AI",
    "batch": "A",

    "city": "Delhi"
}
print("Name:", student["name"])
print("Course:", student["course"])

numbers = list(range(1, 11))
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

words = ["python", "ai", "python", "data", "ai", "python"]

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)