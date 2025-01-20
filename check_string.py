str1 = input("Enter a sentence: ")
substr = input("Enter a word to be searched in the sentence: ")

if substr in str1:
    print(substr, " is present in ", str1)