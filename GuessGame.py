import random
difficulty = random.randint(1, 5)
secret_number = random.randint(1,5)

user_guess = int(input("Enter Guess Number : 1-5 "))
if user_guess > 6 :
   print("Erorr the number over the 5 ")
elif user_guess != secret_number :
    print("False " , secret_number)
else:
  print("true " , secret_number)
