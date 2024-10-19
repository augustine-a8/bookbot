def get_contents(path):
    with open(path) as p:
        return p.read()

def get_words(string):
    return len(string.split())

def get_character_count(string):
    character_count = {}
    for word in string.split():
        for character in word:
            lowercase_char = character.lower()
            if lowercase_char in character_count:
                character_count[lowercase_char] += 1
            else:
                character_count[lowercase_char] = 1

    return character_count

def sort_on(dict):
    return dict["count"]

def sort_character_dict(character_count):
    characters = []
    for k in character_count:
        characters.append({"char": k, "count": character_count[k]})
    characters.sort(reverse=True, key=sort_on)
    return characters
    

def generate_report(path, word_count, character_count):
    print(f"------- Begin report of {path} -------")
    print(f"{word_count} words found in the document")
    print("")
    for dict in character_count:
        character = dict["char"]
        count = dict["count"]
        print(f"The {character} character was found {count} times")



def main():
    book_path = 'books/frankenstein.txt'
    contents = get_contents(book_path)
    words = get_words(contents)
    character_count = get_character_count(contents)
    sorted_characters = sort_character_dict(character_count)
    generate_report(book_path, words, sorted_characters)

main()