
frontend_students = {"Anu", "Rahul", "Meera", "Arjun"}
backend_students = {"Rahul", "Kiran", "Meera", "Sanjay"}


backend_students.add("Akhil")


frontend_students.remove("Arjun")


both_courses = frontend_students.intersection(backend_students)


only_backend = backend_students.difference(frontend_students)


total_students = frontend_students.union(backend_students)


course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}


print("Frontend Students:", frontend_students)
print("Backend Students:", backend_students)

print("Students enrolled in both courses:", both_courses)

print("Students only in Backend:", only_backend)

print("Total unique students:", len(total_students))


print("\nCourse Enrollment Counts:")
for course, count in course_counts.items():
    print(course, ":", count)


new_courses = {
    course: count for course, count in course_counts.items()
}

new_courses["Fullstack"] = (
    course_counts["Frontend"] + course_counts["Backend"]
)

print("\nUpdated Course Dictionary:")
print(new_courses)