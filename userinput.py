def weather_condition(temprature):
    if temprature > 7:
        return "Warm"
    else: 
        return "Cold"
user_input = int(input("Enter temprature:"))
print(weather_condition(user_input))

#greet = input("Enter your name:")     My simple code to diplay input message
#print("Hello", greet,"Welcome to the Course!")

# Another way of displaying message introduced in pytthon 2 & 3 is %s string:
# %s string valid for python 2 & 3

user_input = input("Enter your name:")
messsage = "Hello %s Welcome to python course!" % user_input
print(messsage) 

#displaying message with a new function f"txt {}" works in python 3.6 & above 
user_input = input("Enter Name:")
messsage = "Hello %s!" % user_input
messsage = f"Hello {user_input} Good Morining!"
print(messsage)

# A code for two user inputs
first_name = input("Enter your First name:")
surname = input("Enter your Surname:")
messsage = "Hi %s %s" % (first_name, surname)  
messsage = f"Hi {first_name} {surname} appriciate!"
print(messsage)

# 3 user input
first_name = input("Enter your First name:")
surname = input("Enter your Surname:")
when = "today"
messsage = "Hi %s %s" % (first_name, surname)  
messsage = f"Hi {first_name} {surname} what's up {when}!"
print(messsage)

dog = input("Enter Dog name:")
messsage = "Hi %s" % dog
print(messsage.title())





