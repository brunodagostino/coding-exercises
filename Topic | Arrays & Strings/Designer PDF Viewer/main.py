def create_map() -> dict[str, int]:
    map = dict()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(len(letters)):
        map[letters[i]] = i

    return map

def check_index(alphabet, letter) -> int:
    return alphabet[letter]

def designer_pdf_viewer(h, word) -> int:
    size = 0
    height = 0

    alphabet = create_map()

    for i in range(len(word)):
        c_index = check_index(alphabet=alphabet, letter=word[i])

        if h[c_index] > height:
            height = h[c_index]
    
    size = height * len(word)

    return size

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = "abc"
size = designer_pdf_viewer(h=h, word=word)
print(size)

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
size = designer_pdf_viewer(h=h, word=word)
print(size)