def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    num_chars = count_chars(file_contents)
    
    char_list = [{"char": key, "count": value} for key, value in num_chars.items()]
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_list:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["count"]} times")

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

def sort_on(dict):
    return dict["count"]

main()