from operator import contains
import re

def first_repeated_word(str):
 
    set_ = set()
    str = re.sub(r'[^\w\s]','', str) 
    print(str)

    str = str.strip()
    str = str.strip('\n')
    str = str.split(" ")
 
    for word in str:
        if word.lower() in set_:
            return word.lower()
        else:
            set_.add(word.lower())
            print(set_)

