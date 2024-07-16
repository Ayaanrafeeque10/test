def count_word_frequency(input_string):
        words = input_string.split()
        word_counts = {}
        for word in words:
         if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
        return word_counts
str1 = "this is a test this is only a test"
frequency_dict = count_word_frequency(str1)
print(frequency_dict)





