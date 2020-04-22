def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean
print(mean([2, 4, 7]))

print(type(mean), type(sum))
#I we don't use return function then O/P is None

def selfmultp(x):
    return x*x
print(selfmultp(7))

def convert(y):
    ounce = 29.56737
    return ounce*y
print(convert(3))


def mean(value):
    if type(value) == dict:       #if isinstance(value, dict) we can also use these instead of type()
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

monday_temprature = [8.8, 9.1, 9.9]
student_grades = {'Merry': 9.1, 'Sam': 8.2, 'Judi': 7.9}
print(mean(monday_temprature))
print(mean(student_grades))


def median(selftest):
    a = len(selftest)
    if a%2==0:
        m1 = selftest[a//2]
        m2 = selftest[a//2]-1
        the_median = (m1 + m2)/2
    else:
        the_median = selftest[a//2]
    return the_median
print(median([2, 5, 11, 8, 9, 10]))
#print(median([3, 7, 12, 9, 12]))

def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False

def temp(temprature):
    if temprature > 25:
        return "Hot"
    elif 25 >= temprature >=15:
        return "Warm"
    else:
        return "Cold" 
print(temp(18))    


message = "hello there"

if "llo" in message:
    print("got it")
else:
    print("I don't understand")

mymessage = "hello everyone"

if "di" in mymessage:
    print("right")
elif "one" in mymessage:
    print("got the answer")
elif "la" in mymessage:
    print("got it")
else:
    print(" I don't understand")
    
        
    

