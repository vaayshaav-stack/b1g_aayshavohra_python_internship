student_record = {
    "name": "john",
    "age": 20,
    "marks": 85.5
}
print(f"original record: {student_record}")

student_record["marks"]=92.0

student_record["grade"]="a"
print(f"updated record: {student_record}")
