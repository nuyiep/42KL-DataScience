
import sys

def check_is_digit(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

if (len(sys.argv) == 1):
	sys.exit()
elif (len(sys.argv) > 2):
	print("AssertionError: more than one argument is provided")
elif (check_is_digit(sys.argv[1]) == False):
	print("AssertionError: argument is not an integer")
elif (int(sys.argv[1]) % 2 == 0):
	print("I'm Even.")
elif (int(sys.argv[1]) % 2 != 0):
	print("I'm Odd.")
