import re
from loader_words import word_list, name_list

candidates = [
    "a dark and stormy night",
    "n qnex naq fgbezl avtug",
    "j mjat jwm bcxavh wrpqc",
    "My name is Yahya",
    "Billy Pilgrim has become unstuck in time",
    "Manchester United is the best team in England.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count


for phrase in candidates:
    word_count = count_words(phrase)
    percentage = int(word_count / len(phrase.split()) * 100)
    if percentage > 50:
        pass
        # print(phrase, percentage)

a_z = ['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z']

def encrypt(sentence, key):
    sentence_encrypt = ""
    sentence_encrypt_second = ""
    sentence_encrypt_third = ""

    for i in sentence.lower():
        sentence_ord = (ord(i) - 97) + key
        sentence_char = (sentence_ord % 26) + 97
        sentence_encrypt += chr(sentence_char)
        
    print(sentence_encrypt)

def decrypt(sentence, key):
    encrypt(sentence, - key)

def crack(sentence):
    # print(sentence)
    pass

print("***********encrypt***********")
encrypt("ABC", 1)
encrypt("abc", 1)
encrypt("abc", 1000)
encrypt("xyz", 4) #aaa

# sentence_encrypt += chr(ord(i) + key) 
print("***********decrypt***********")
decrypt('bcd', 1)
decrypt('bcd', 1)
decrypt('mno', 1000)
decrypt('aaa', 1)

