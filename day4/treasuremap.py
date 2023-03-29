row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_num = int(str(position[0]))
second_num = int(str(position[1]))

if first_num == 1:
    if second_num == 1:
        row1[0] = "X "
    elif second_num == 2:
        row2[0] = "X "
    elif second_num == 3:
        row3[0] = "X "
        
elif first_num == 2:
    if second_num == 1:
        row1[1] = "X "
    elif second_num == 2:
        row2[1] = "X "
    elif second_num == 3:
        row3[1] = "X "

if first_num == 3:
    if second_num == 1:
        row1[2] = "X "
    elif second_num == 2:
        row2[2] = "X "
    elif second_num == 3:
        row3[2] = "X "
 


print(map[0])
print(map[1])
print(map[2])
# print(map)
# print(first_num)
# print(second_num)
