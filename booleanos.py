## booleano
## <    >   <=  >=  ==  !=

var1 = True
var2 = False
print(var1)
print(var2)
print(type(var2))

print("--------------------")

num = 5 > 2+3
# num = 5 == 2+3
# num = 5 != 2+3
print(type(num))
print(num)

print("--------------------")

num = bool(5>6)
# num = bool(5<6)
print(type(num))
print(num)

print("--------------------")

list = [1,2,3,4]
control = 5 in list
# control = 5 not in list
print(type(control))
print(control)