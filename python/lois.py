print("Hello World!")
_myCompany = "Eliraz Limited"
myWebsite = "Consultancy firm"
age = 2
print(type("MyCompany"))
print(type(age))
aStartup =True
aPublicEntity = False
print("My company's name is", _myCompany)
print("My Company's name is %s It is a %s" % (_myCompany, myWebsite))
print("Welcome to my First Website")
print("Its a Website to help you solve all your organisational worries")
print("We render Services like IT consultancy, Financial Services and Business Analysis")
print("You can book by simply clicking on the Book option")
print("Thank you,and I look forward to having you as a client")

def sum( first,second):
    sum = first + second
    return(sum)

print (sum(5, 19))

def calculate (action, first, second):
    result = first + second
    return result

calcResult = calculate("add", 10, 5)
calcResult = calculate("add", calcResult, 50)
print(calcResult)

def find (do, first, second):
    if do == "sum":
        answer = first + second
        return answer
    elif do == "minus" :
        answer = first - second
        return answer
    elif do =="multiply":
        answer = first * second
        return answer
    else :
        answer = first // second
        return answer

findanswer = find("minus", 15, 5)
findanswer = find("sum", findanswer, 5)
findanswer = find("multiply", findanswer, 4)
findanswer = find("divide", findanswer, 2)
print("The answer is:", findanswer)

number =1
while number <= 20 :
    print("Number:", number)
    number += 1

for number in range(10, 20, 2) :
        print("Number:", number)

services = [ "Financial", "IT consultancy", "Business Analysis" ]
for service in services:
        print("Service is:", service)
print("Our loop is done!")



