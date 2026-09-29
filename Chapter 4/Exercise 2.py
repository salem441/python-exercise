# Exercise 2: Move the last line of this program to the top, so the function call
# appears before the definitions. Run the program and see what error message you
# get.

repeat_lyrics()


def print_lyrics():
    print("i am a lumberjac")
    print('I sleep all night and i work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()
# NameError: name 'print_lyrics' is not defined

