
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
    for char in uses:
        for letter in word:
            if letter == char:
                print("True")
    else:
        print("False")
            
            
                
        

#avoids("ouch","ouch") 
#count_avoids('zxquw')   
uses_only('frog','frog')