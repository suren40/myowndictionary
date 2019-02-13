#!usr/bin/env python3
"""
This is show me the file what i need

"""
import wordlist as wordlist
def search(word):
    try:
        print(word,":")
        print(wordlist.wordlist[word.upper()])
    except KeyError:
        print("not found")


if __name__ == "__main__":
    print("The meaning I use to read which is personal")
    print("-"*50)
    word = input("\n Search the word : ")
    print("*"*50)
    print(search(word))
