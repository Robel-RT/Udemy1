import datetime
mydate = datetime.datetime.now()
print(mydate)

mynumber =  20
mytext = "Hello!"
print(mynumber, mytext)

x = 10
y = "10"
z = 5.3
sum1 =  x + x
sum2 = y + y
sum3 = z + z
print(sum1, sum2)
print(type(x), type(y), type(z))

student_grades = [9.1, 8.8, 7.5]
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum/length 
print(mean)

m1 = mysum/2
m2 = (mysum/2)-1
median = (m1 + m2)/2
print(median)

student_grades = {"Merry": 9.1, "Sim": 8.8, "Steven": 7.5}
mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length
print(mean)

student_grades = {"Merry": 9.1, "Sim": 8.8, "Steven": 7.5}
print(student_grades.keys())
#These keys() prints out the keys in the dictionary Merry...

#Tuples 
monday_temprature = (1, 4, 5)
print(monday_temprature)

day_temprature = {"morning": 3.5, "noon": 4, "evening": 5}
print(day_temprature)

color_codes = ((1,3,6), (5,5,7), (9,3,6))
print(color_codes)

day_temprature2 = {'morning': (1.2,1.9,2), 'noon': (2.2,2.5,3), 'evening': (3.5,4.0,4.7)}
print(day_temprature2)
# a dictionary with tuples and tuples with each value
 





