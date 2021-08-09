"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
#import pytest

def no_duplicates(a_string):
    my_list = sorted(set(a_string))
    return my_list


def reversed_words(a_string):
    reverse = (a_string[::-1])
    return reverse


def four_char_strings(a_string):
    n = 4
    string_return = ([a_string[i:i+n] for i in range(0, len(a_string), n)])
    return string_return


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

print(no_duplicates("shgdshgd"))

print(reversed_words("Hello World"))

print(four_char_strings("this is the sentence of segev"))

"""
def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
"""
