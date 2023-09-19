
import sys

def main():
	if (len(sys.argv) != 3):
		print("AssertionError: the arguments are bad")
		sys.exit()
	if (sys.argv[1] == None or sys.argv[2] == None):
		print("AssertionError: empty content")
		sys.exit()
	if (sys.argv[2].isdigit() == False):
		print("AssertionError: the arguments are bad- not digit")
		sys.exit()
	word_list = sys.argv[1].split(' ')
	all_word_count = []
	for word in word_list:
		if word.isalpha() == False:
			print("AssertionError: the arguments are bad- not alpha")
			sys.exit()
		word_count = len(word)
		if (word_count > int(sys.argv[2])):
			all_word_count.append(word)
	print(all_word_count)

if __name__ == "__main__":
	main()
