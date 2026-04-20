
#creat a program that evaluates the strength of a user's password based on its length. The program should prompt user to enter a password, analyse its length , and classify it into one of four categories: 'very weak', 'weak' , 'Strong', or 'very strong'
#
#password length         Strength
#
#< 8                     very weak
# 8                      weak
#bet. 8 & 16             strong
#Above 16                very strong
#
#
name = "b"
name = bool(name)
print(name)

user_password = input("Enter your password:" )

length = len(user_password)  
       
if length < 8:
   print("very weak")

elif length == 8:
    print ("weak")

elif length >= 8 and length <= 16:
    print("strong")

elif length > 16:
    print("very strong")

else:
    print(" ")

#user_name = "Bro Code"
#print(f"Your username is {user_name}")
#
#year = 2024
#print(f"You were born in year {year}")
#
#pi = 3.14
#print(f"The value of pi is {pi}")
#
#
#is_admin = False
#print(f"Is She around? {is_admin}")
#
#if is_admin:
# print("She is around")
#
#else:
# print("She is not around")
#


#def get_name(user_name):
#    return user_name
#
#print(get_name("Bro Code"))

#def get_sum_of_numbers(a,b):
#    sum = a+b 
#    return sum
#
#print(get_sum_of_numbers(2,3))
#
#
