age = 25
name = "Shinya"
print(age)

print('I am {} I am {} years old'.format(name, age))

if age > 18:
  print("You are older than 18")
else :
  print("You are younger than 18")

if name == "Shinya":
  print("My name is Shinya")

#これはコメントです
"""複数業の時は
こう書きます。"""

def hello(thestring):
  print("Hello world!")
  return'Hello ' + thestring

sentence = hello('taro')
print(sentence)

foodname = ["chocolate", "cake", "bisket", 21]
print(foodname)
foodname.insert(0, "donats")
print(foodname)
print(foodname[2])
del(foodname[2])
print(foodname)
print(len(foodname))

for food in foodname:
  print(food)

for number in range(1,10):
  print(number)

age2 = 0
while age2 < 10:
  print(age2)
  age2 += 1

dogs = {"poti":5, "shiro":8, "inu":1}
dogs["sarah"] = 6

print(dogs)
print(dogs["poti"])

class Dog:
  def __init__(self, name, age, color):
    self.name = name 
    self.age = age
    self.color = color

  def bark(self):
    print("wan,wan")

mydog = Dog("taro", 15, "white")
mydog.bark()
print(mydog.age)