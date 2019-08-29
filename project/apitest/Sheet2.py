import openpyxl

# Location of the file
from project.apitest.Sheet1 import list_of_lists

path = 'C:/Users/melikyan.tatevik/Desktop\megafeed_test_app/Soccer.xlsx'

# To open the workbook
wb = openpyxl.load_workbook(path)

# Get workbook active sheet
sheet = wb.active

wb.title = "Sheet2"

# Rows to lists
row_list1 = [row for row in sheet.values]
# print(row_list)

list_of_lists1 = [list(elem) for elem in row_list1]
print(list_of_lists)

for item in list_of_lists1:
    if item[3] == None:
        item[3] = ''

for item in list_of_lists1:
    if item[4] == None:
        item[4] = ''

for item in list_of_lists1:
    if item[2] == '1/2':
        item[2] = item[2].split('/')
        item[2] = [int(elem) for elem in item[2]]
        # print(item[2])
