from Python import my_module
from Python import mod1

greet = my_module.greeting_msg()
print(greet)

name = my_module.get_name()
print(name)

course = my_module.get_course()
print(course)

print("-----------------------------------")

print(mod1.testAdd(4,5))
print(mod1.testSub(4,5))
print(mod1.testMul(4,5))
print(mod1.testDiv(4,5))
print(mod1.testLength("chandra"))