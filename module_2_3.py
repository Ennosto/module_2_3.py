my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    num = my_list[index]
    index = index + 1
    if num == 0:
        continue
    elif num < 0:
        break
    elif num == len(my_list):
        print(num)
    else:
        print(num)