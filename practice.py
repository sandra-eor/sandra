name = ["Jaden","Karl","Andy","Sophi"]

def printages():
    guess = input("Are you Jaden,Karl,Andy,Sophi?Yes/No:")
    while guess == "Yes".lower():
                yesguess = (input("Who you are?"))
                if yesguess.lower == [""]:
                        print("Welcome, a great party")
                elif yesguess == "no".lower:
                        print("Sorry you're not guess in this party")
                        


   # elif age <= 19:
   #     print("You are not elegible!.Wait a little longer")

    #else:
    #    print(printages)


if __name__=="__main__":
    printages()