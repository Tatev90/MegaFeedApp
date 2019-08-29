import openpyxl

# Location of the file
from project.apitest.main import current_game

path = 'C:/Users/nuard.atabekyan/Desktop/Soccer.xlsx'

# To open the workbook
wb = openpyxl.load_workbook(path)

# Get workbook active sheet
sheet = wb.active

wb.title = "Sheet4"

# Rows to lists
row_list3 = [row for row in sheet.values]
# print(row_list3)

list_of_lists3 = [list(elem) for elem in row_list3]
# print(list_of_lists3)

for item in list_of_lists3:
    if item[2] == '1/2':
        item[2] = item[2].split('/')
        item[2] = [int(elem) for elem in item[2]]
        # print(item[2])

ls = []
for item2 in current_game:
    if item2[0] == 233:
        ls.append(item2)
# print(ls)

ls1 = []
for i in ls:
    x = i[4][6:9]
    y = i[4][15:18]
    x = x.replace('"', '')
    y = y.replace('"', '')
    ls1.append(x)
    ls1.insert(2, y)
print(ls1)

for i in ls1:
    i_even, i_odd = ls1[::2], ls1[1::2]
    for j in i_even:
        for k in i_odd:
            item_four = item[4].replace('ddd', j).replace('nnn', k)
            print(item_four)
