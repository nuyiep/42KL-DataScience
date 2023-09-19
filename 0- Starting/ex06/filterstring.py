
import sys

def format_checking():
	'''
		Check if the first argv is a string
		Check if the second argv is an int
		If not, exit the program
	'''
	if (len(sys.argv) != 3):
		print("AssertionError: the arguments are bad")
		sys.exit()
	if (sys.argv[1] == None or sys.argv[2] == None):
		print("AssertionError: empty content")
		sys.exit()
	for char in sys.argv[1]:
		if (char.isalpha() == False and char != ' '):
			print("AssertionError: not an alphabet")
			sys.exit()
	if (sys.argv[2].isdigit() == False):
		print("AssertionError: the arguments are bad- not digit")
		sys.exit()

def ft_filter():
	'''
		in python- filter(function, iterable)
		returns items from iterable based on some criteria
	'''
	word_list = sys.argv[1].split(' ')
	all_word_count = [word for word in word_list 
				   if (lambda word: len(word) > int(sys.argv[2]))(word)]
	# for word in word_list:
	# 	word_count = len(word)
	# 	if (word_count > int(sys.argv[2])):
	# 		all_word_count.append(word)
	return all_word_count

def main():
	'''
		format checking then filter the words
		then print
	'''
	format_checking()
	all_word_count = ft_filter()
	print(all_word_count)

if __name__ == "__main__":
	main()
