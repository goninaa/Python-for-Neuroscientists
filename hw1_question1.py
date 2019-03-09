def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    count = 0
    i = 0
    while i < (len(word)-1):
        if word[i] == word[i+1]:
            count+=1
            i +=2
            if count>= 3:
                return True
        
        else:
            count = 0
            i+=1
            
    return False



if __name__ == '__main__':
    # Question 1
    word = 'gaabbhccd'
    return_value = trifeca(word)

    print(f"Question 1 solution: {return_value}")




