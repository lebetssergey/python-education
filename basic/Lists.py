numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
i = 1 
for x in range(3):
    numbers.append(i)
    i+=1

strings.append('hello')
strings.append('world')

second_name = names[1]
print(*numbers)
print(strings)
print("The second name on the names list is %s" % second_name)