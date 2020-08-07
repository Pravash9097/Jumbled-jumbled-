#all jumbled words
que=['adhn','npe','irha','yee','sace','anf','mite','oty', 'rapep','lewot','tighl','pesha','triks','tchaw', 'metyss','paptol','wiollp','suerotr','dreba','rmiror']
#all correct words
ans=['hand','pen','hair','eye','case','fan','time','toy', 'paper','towel','light','shape','skirt','watch', 'system','laptop','pillow','trouser','beard','mirror']
#begin function to show rules etc
def begin():
    print('WELCOME TO BAIN_DICTIONARY')
    print('Rules: \n 1) Give it a try. \n 2) For right you will get 10 points. \n 3) Every wrong answer will lose one life')
    choice = input("\nPress any key to continue: ")
def game():
    score=0
    life=2
    i=0
    while(life !=0 and i<len(que)):
        x=input(que[i])
        if(x==ans[i]):
            score=score+10
            print('RIGHT answer')
            print('new score=',score)
        else:
            life=life-1
            print('Wrong answer \n you loss a life')
        i=i+1
    else:
        print("\n\nGAME OVER")
        print("Final Score = ",score)
        next = input("\n\nDo you want to play again? Press Y for yes any key for No: ")
        if (next=='Y' or next=='y'):
          play()
        else:
          exit()
def play():
    begin()
    game()
play()
