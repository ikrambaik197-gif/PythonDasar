class person:
 def _init_(self, name, age):
  self.name = name
  self.age = age

 def myfunc(self):
  print("Hello my name is "+ self.name)

p1 = person("John", 36)
p1.myfuncS