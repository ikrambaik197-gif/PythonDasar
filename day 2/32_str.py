class person:
 def _init_(self, name, age):
  self.name = name
  self.age = age

 def _str_(self):
  return f"{self.name}({self.age})"
p1 = person ("John", 36)
print(p1)