# 42KL-DataScience

**Filter**
filter function - filter(function, iterable)
 				  - returns items from iterable based on some criteria

age = [5, 12, 17, 18, 24, 32]

def myFunc(x):
	if x < 18:
		return False
	else:
		return True

adults = filter(myFunc, age)

for x in adults:
	print(x)

**List comprehension**
From this 
	nums = [54, 22, 15, 48]
	evens = []
	for num in nums:
		if num % 2 == 0:
			evens.append(num)
	print(evens)

To this
	evens = [num for num in nums if num % 2 == 0]

	print(evens)

**Lambda**
From this
	def add(x, y):
		return x+y
	print(add(1, 2))

To this
	print((lambda x,y: x+y)(1,2))
