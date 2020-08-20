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