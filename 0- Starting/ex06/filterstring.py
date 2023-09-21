
import sys


def format_checking():
    '''
        Check if the first argv is a string
                     second argv is an int
    '''
    try:
        assert len(sys.argv) == 3
        assert sys.argv[1] is not None or sys.argv[2] is not None
        for char in sys.argv[1]:
            assert (char.isalpha() is True or char == ' ')
        assert sys.argv[2].isdigit() is True
    except Exception:
        print("AssertionError: the arguments are bad")
        sys.exit()


def main():
    '''
        format checking then filter the words
    '''
    format_checking()
    words = sys.argv[1].split(' ')
    length = int(sys.argv[2])
    word_count = [i for i in words if (lambda i: len(i) > length)(i)]
    # all_word_count = ft_filter(lambda word: len(word) > len_argv2, word_list)
    # for word in word_list:
    # 	word_count = len(word)
    # 	if (word_count > int(sys.argv[2])):
    # 		all_word_count.append(word)
    print(word_count)


if __name__ == "__main__":
    main()

# if we handle negative number, our split function needs to be general (consider all white spaces)