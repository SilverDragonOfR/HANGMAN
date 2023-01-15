program=True
while (program==True) :

    count=0
    print("Welcome to HANGMAN !!!")
    lword=list(input("Enter the word to be found: "))
    lcheck=[]
    
    for i in range(len(lword)):
        lcheck.append(0)

    for i in range(100):
        print()

    game=True
    while (game==True):

        print("WORD ==",end=" ")
        for i in range(len(lword)):
            if (lcheck[i]==0):
                print("*",end=" ")
            else:
                print(lword[i],end=" ")
        print()

        uchar=input("Guess a letter: ")
        count=count+1

        if (uchar in lword):
            print("YES CORRECT")

            for j in range(len(lword)):
                if (lcheck[j]==0 and lword[j]==uchar):
                    lcheck[j]=1
                    break

        else:
            print("NO WRONG")

        if (0 not in lcheck):
            game=False


    print("FINAL WORD IS ==",end=" ")
    for i in range(len(lword)):
        print(lword[i],end=" ")
    print()

    print("YOU took",count,"turns to guess the word")

    ch=input("Do you want to play again (Y/N): ")
    if (ch=="N"):
         program=False


    if (program==True):
        print()
        print()


        
            

    
        
