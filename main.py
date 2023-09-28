PATH = 'books/frankenstein.txt'
with open(PATH) as f:
    file_contents = f.read()
    words = file_contents.split()
    letter_count = {}
    letters = [letter for letter in file_contents.lower()]
    letters.sort()
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        elif letter not in letter_count and letter.isalpha():
            letter_count[letter] = 1
    ordered_letters = sorted(
        letter_count.items(), key=lambda x: x[1], reverse=True
        )
    print(f'--- Begin report of {PATH} ---')

    for item in ordered_letters:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")
