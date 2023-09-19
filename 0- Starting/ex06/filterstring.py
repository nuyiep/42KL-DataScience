
import sys

def format_checking():
	'''
		Check if the first argv is a string
					 second argv is an int
	'''
	try:
		assert len(sys.argv) == 3
		assert sys.argv[1] != None or sys.argv[2] != None
		for char in sys.argv[1]:
			assert (char.isalpha() == True or char == ' ')
		assert sys.argv[2].isdigit() == True
	except:
		print("AssertionError: the arguments are bad")
		sys.exit()

def main():
	'''
		format checking then filter the words
	'''
	format_checking()
	word_list = sys.argv[1].split(' ')
	all_word_count = [word for word in word_list 
				   if (lambda word: len(word) > int(sys.argv[2]))(word)]
	# for word in word_list:
	# 	word_count = len(word)
	# 	if (word_count > int(sys.argv[2])):
	# 		all_word_count.append(word)
	print(all_word_count)

if __name__ == "__main__":
	main()
