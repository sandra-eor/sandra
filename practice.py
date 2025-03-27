#The list of positions
positions =["secretary","human resources","cleaning", "painter","computer installer"]
certified="secretary","human resources","computer installer"
n_certified ="cleaning", "painter" 

#Print and enter the positions
def position(certified,n_certified):
    print("Hello dear friend! We have vacancies for these positions")
    print(','.join(positions))

#The user will know if it  is suitable for the position
    while True:
        puw = str(input("What position would you like to apply for?")).strip().lower()
        if  puw in certified:
            print("You need to have a minimum high school certificate for this position.")
            cer = str(input("Do you have certificate?Yes/No:")).strip() .lower()
            if cer =="yes":
                break
            elif cer == "no":
                print("Sorry, you need it.")
            else:
                print("Wrong answer!!.Try again")
                print(position(certified,n_certified))

        elif puw in n_certified:
            exp = input("Do you have experience?Yes/No:").strip().lower()
            if exp =="yes":
                break
            elif exp == "no":
                print("Sorry, you need it.")
            else:
                print("Wrong answer!!.Try again")
                print(position(certified,n_certified))
        
        else:
            print("Wrong answer!!Try again")
#Lists of accepted ages
ages = [20, 21, 22,23,24, 25]
min = 20
max = 25

def age_s(min ,max):# These parameters identify the maximum age and minimum age that the user could have.
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
            print(position(certified,n_certified))
        else:
            print("Sorry, you are not eligible for this position.")
            print(position(certified,n_certified))

    print("Thank you for trying!")
#call the functions so that the codes can run
position(certified,n_certified)
age_s(min,max)


