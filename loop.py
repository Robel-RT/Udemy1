monday_temprature = [9.1, 8.8, 7.6]

for temprature in monday_temprature:
    print(round(temprature))


my_number = [7.3, 9.4, 10.1,]
for number in my_number:
    print(round(number))
    print("Done")


for letter in "hello":
    print(letter.title())


def celsius_to_kelvin(cels):
    return cels + 200.1

monday_temprature = [9.1, 8.8, 7.6]
for temprature in monday_temprature:
    print(celsius_to_kelvin(temprature))

student_grades = {"Judi": 9.3, "Sam": 8.7, "Alex": 8.9}
for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

store = [23, 5.6, 7, 11]
for i in store:
    print(i)

username = ""
while username != "pypy":
    username = input("Enter username: ")
    print(username)
    if username == "pypy":
        print("Done")
        break
    else:
        continue
    
# Another way of writing above code
while True:
    username = input("Enter username: ")
    print(username)
    if username == "pypy":
        print("operation aborted!")
        break
    else:
        continue



