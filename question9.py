def unique_words(word_list):
    unique_set = set(word_list)  
    unique_list = list(unique_set)  
    return unique_list

if __name__ == "__main__":
    words = input("Enter a list of words separated by spaces: ").split()
    unique_words_list = unique_words(words)
    print("Unique words:", unique_words_list)