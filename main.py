def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    print(num_words)

def count_words(text):
    words = text.split()
    return len(words)
main()