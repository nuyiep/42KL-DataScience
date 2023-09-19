import sys

def error_checking():
	try:
		assert len(sys.argv) == 2, "the arguments are bad"
		for char in sys.argv[1]:
			assert char.isalnum() or char == ' ', "argv1 is not alphabet"
	except AssertionError as message:
		print("AssertionError:", message)
		sys.exit()

def convert_into_morse_code():
	morse_code_dict = {
		' ': '/', 'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--','Z': '--..',
        '0': '-----','1': '.----','2': '..---',
		'3': '...--','4': '....-','5': '.....',
        '6': '-....', '7': '--...','8': '---..', '9': '----.'
	}
	length = len(sys.argv[1])
	count = 0
	for char in sys.argv[1].upper():
		if char in morse_code_dict.keys():
			print(morse_code_dict[char], end='')
			count += 1
		if count != length:
			print(' ', end='')
		else:
			print("\n", end='')

def main():
	error_checking()
	convert_into_morse_code()
		
if __name__ == "__main__":
	main()
