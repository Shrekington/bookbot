def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    num_chars = count_chars(file_contents)
    print(num_words)
    print(num_chars)

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    num_chars = {}
    chars = text.lower()
    
    for char in chars:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    
    return num_chars


main()