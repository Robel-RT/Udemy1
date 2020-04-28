def sentence_maker(phrase):
    Interogatives = ("How", "What", "Why", "When")
    capitalized = phrase.capitalize()
    if phrase.startswith(Interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Enter your statement: ")
    if user_input == "end":
         break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))

# Example of Join method
h1 = input("Enter first name: ")
h2 = input("Enter second name: ")
message = f" {h1} - {h2}"

print("".join(message))


temps = [321, 456, 873, 764]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

# Short way of above code
temps = [321, 456, 873, 764]

new_temps = [temp/10 for temp in temps]
print(new_temps)



temprature = [342, 675, -996, 452, 1278, -555]

new_scale = [temp/10 if temp > 0 else 0 for temp in temprature]   #puts 0 inplace on any negative number
print(new_scale)


my_list = [-2, 3, 4, -21, 6, -6]

new_list = [i for i in my_list if i > 0]
print(new_list) 


pad = ['2,1', '3.5', '4.9']

num = [sum([float(i) for i in pad])]
print(num) 

   