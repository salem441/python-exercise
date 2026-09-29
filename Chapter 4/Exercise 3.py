# Exercise 3: Move the function call back to the bottom and move the definition
# of print_lyrics after the definition of repeat_lyrics. What happens when you
# run this program?


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("i am a lumberjac")
    print('I sleep all night and i work all day.')


repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined

