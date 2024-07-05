import random
Password = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:''"
Length_Password = int(input("Enter the Length of password : "))

a = "".join(random.sample(Password, Length_Password))

print(f"Your Password is : {a} ")