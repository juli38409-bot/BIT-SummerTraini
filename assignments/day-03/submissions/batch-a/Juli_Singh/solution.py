students = ["Aman", "Priya", "Rahul", "Neha", "Vikas"]
print("Students:", students)

students.append("Ansh")
print("After adding:", students)

cities = ("Delhi", "Mumbai", "Lucknow", "Pune", "Chennai")
print("Second city:", cities[1])

courses = {"Python", "Java", "C++", "AI", "ML"}
courses.add("Data Science")
print("Courses:", courses)

student = {
    "name": "Juli",
    "branch": "CSE",
    "batch": "2026",
    "marks": 85
}

for k, v in student.items():
    print(k, ":", v)