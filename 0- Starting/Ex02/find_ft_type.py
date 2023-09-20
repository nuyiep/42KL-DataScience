
# this function accepts 1 argument named object of any type
# return an int 
def all_thing_is_obj(object: any) -> int:
	type_of_parameter = type(object)
	if (isinstance(object, str)):
		print(object, "is in the kitchen :", type_of_parameter)
	elif (isinstance(object, int)):
		print("Type not found")
	elif (isinstance(object, float)):
		print("Type not found")
	else:
		print(type_of_parameter.__name__.capitalize(), ":", type_of_parameter)
	return 42
