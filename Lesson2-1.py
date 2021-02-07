print('Введите строку')
text = str(input()).split()
count = 0
for i in text:
    if len(i) > count:
        count = len(i)
        world = i
print(world)
