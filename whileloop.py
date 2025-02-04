total = 0
count = 0

userInput= input("Please enter a number:")

while userInput != "done":
    userInput = input("Please enter a number:")
    count =+ 1
    if userInput !="done":
        total += int(userInput)
       
   


print("Running overage:", total / count)
