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

#Example of Join method
h1 = input("Enter first name: ")
h2 = input("Enter second name: ")
message = f" {h1} - {h2}"

print("".join(message))




    


        


    


