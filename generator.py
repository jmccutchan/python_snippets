#This example uses generator functions and yields a generator instead of returning a list
#use 'yield' instead of 'return' - yield a generator instead of returning a list, this consumes less memory

def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

ipsum = "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

it = index_words(ipsum)
print(it) #returns a generator (iterator) object

print(next(it)) #returns each consecutive iterable


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

address = """ Four score and seven years ago our fathers brought forth on this
continent a new nation, conceived in liberty, and dedicated to the proposition that
all are created equal."""

with open('/tmp/address.txt', 'w') as f:
    f.write(address)

with open('/tmp/address.txt') as f:
    it = index_file(f)
    print(next(it)) #returns the next index
    print(next(it)) #returns the next index
    print(list(it)) #returns everything in a list