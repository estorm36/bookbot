def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def num_letters(text):
    full = text.lower()
    empty = {}
    for i in full:
        if i.isalpha(): 
            if i in empty:
                empty[i] = empty[i] + 1
            else:
                empty[i] = 1
    return empty

def report(path, text):
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document\n")
    char_counts = num_letters(text)
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse = True, key = sort_on)

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times ")
    print("--- End report ---")

if __name__ == "__main__":
    text = main()
    word_count = count_words(text)
    char_count = num_letters(text)
    report("books/frankenstein.txt", text)
    '''print(word_count)
    print(char_count)'''


