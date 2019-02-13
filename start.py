#!usr/bin/env python3
"""
This is show me the file what i need

"""
import wordlist as wordlist
def search(word):
    print(word.upper())
    print(wordlist.wordlist[word.upper()])

if __name__ == "__main__":
    print("welcome find the word")
    word = input("\n Your word ")
    print(search(word))
