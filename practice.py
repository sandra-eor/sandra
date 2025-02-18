"""names = ["Jaden","Maicol","Karen",Larissa"]
def printsomething():
    guess = input("Are you Jaden,Maicol,Karen,Larissa?Yes/No:")
    while True:
        
       if guess == "Yes".lower():
                yesguess = (input("Who you are?"))
                if yesguess.lower in names:
                        print("Welcome, a great party")
                        break
                else:
                        print("Sorry you're not guess in this party")
                        
        

   # elif age <= 19:
   #     print("You are not elegible!.Wait a little longer")

    #else:
    #    print(printages)


    """


#def position(self):
   # self.print("")

positions =["secretary","human resources","cleaning", "painter","computer installer"]
certified="secretary","human resources","computer installer"
n_certified ="cleaning", "painter"

def position(certified,ncertified):
    print("Hello dear friend! We have vacancies for these positions")
    print(positions)

    while True:
        puw = str(input("What position would you like to apply for?"))
        if  puw == certified:
            print("Necesitas tener certificado para estas posiciones ")
        

ages = [20, 21, 22,23,24, 25]
min = 20
max = 25
def age_s(min ,max):
    print("Welcome! Please enter your age to see if you are eligible for the position.")



    while True:
        userage = int(input("How old are you(20,21,22,23,24,25)?"))

        if userage < min:
            print("Sorry, you are not eligible. You must be at least  20 years old..Wait a little longer")
        elif userage in ages:
            print("Congratulations! You are eligible and accepted for the position.")
            break
        elif userage > max:
            print("Sorry, you are too old for this position.")
        else:
            print("Sorry, you are not eligible for this position.")

    print("Thank you for trying!")


age_s(min,max)


