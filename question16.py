def is_palindrome(sentence):
        clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
        return clean_sentence == clean_sentence[::-1]
sentence1 = "a man a plan a canal Panama"
sentence2 = "hello world"
print(f"Is '{sentence1}' a palindrome? {is_palindrome(sentence1)}")
print(f"Is '{sentence2}' a palindrome? {is_palindrome(sentence2)}")



