import re

def first_repeated_word(str):
 
    set_ = set()
    str = re.sub(r'[^\w\s]','', str)
    str = re.sub(r'\n', '', str) 
    str = str.split(" ")
    
    print(str)
    for word in str:
        if word and word.lower() in set_:
            return word.lower()
        else:
            set_.add(word.lower())
            print(set_)

