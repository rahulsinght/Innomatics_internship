  
def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ str(S))
    elif K>S:
        print("Kevin"+" "+str(K))
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)