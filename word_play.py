import re

def at_least():
    '''
    prints only the words with at least 20 words
    '''
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) > 19:
                    print(word)
                    count += 1
                    print(count)

def has_no_e():
    '''
    prints all the words with no 'E'
    '''
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if "e" not in word:
                    print(word)

def avoids(word,forbid):
    '''
    Takes word, takes string of forbidden letters,
    returns True if word free of forbidden letters
    '''
    for j in range(len(forbid)):
        for i in range(len(word)):
            if forbid[j] == word[i]:
                return False
                print("False")
    else:
        return True
        print("True")
            

def count_avoids(forbid):
    count = 0
    word_count = 0
    '''
    prints number of words without
    forbidden letters entered by user
    '''
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                word_count += 1
                for j in range(len(forbid)):
                    for i in range(len(word)):
                        if forbid[j] == word[i]:
                            count += 1
        print(word_count - count)
                            
                            
                        
    

def uses_only(word,uses):
    '''
    
    '''
    o = False
    for char in uses:
        for letter in word:
            if letter == char:
                o = True
                
            if letter not in uses:
                o = False
                break
    return o

def words_with_only(uses):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,uses):
                    print(word)
            
def uses_all(word,letters):
    '''
>>> uses_all('return','re')
True
        
    '''
    for char in letters:
        for letter in word:
            if char not in word:
                return False
    else:
        return True

def how_many_uses_all(letters):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word,letters):
                    print(word)

def is_abcedarian(word):
    '''
    >>> is_abcedarian('word')
    False
    
    >>> is_abcedarian('abce')
    True
    >>> is_abcedarian('stuv')
    True
    '''
    word = word.lower()
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
            return False
    return True

def count_abecedarian():
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abcedarian(word):
                    count += 1
                    
    return count
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #words_with_only('acehflo')
    #print(uses_only('ffffffffffffrg','frg'))
    #print(uses_all('return','re'))
    #print(is_abcedarian('word'))
    #count_abecedarian()
#avoids("ouch","ouch") 
#count_avoids('zxquw')   
#uses_only('frog','frog')
