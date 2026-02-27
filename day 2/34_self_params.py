class person:
 def _init_(mysillyobject, name, age):
   mysillyobject.name = name
   mysillyobject.age = age

 def myfunc(abc):
   print("Hello my name is" + abc.name)

p1 = person("john", 36)
p1.myfunc()