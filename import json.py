import json 
Student_data={"name":"David","age":13,"marks":98}
print(type(Student_data))
data=json.dumps(Student_data)
print(data)
print(type(data))
