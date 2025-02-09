def minion_game(string):
    n=len(string)
    kevin_score,stuart_score=0,0
    for i in range(n):
        if string[i] in "AEIOUaeiou":
            kevin_score+=(n-i)
        else:
            stuart_score+=(n-i)
            
    if kevin_score>stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score==stuart_score:
        print('Draw')
    else:
        print(f"Stuart {stuart_score}")

if __name__ == '__main__':
    s = input()
    minion_game(s)