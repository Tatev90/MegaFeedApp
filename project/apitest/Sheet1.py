import openpyxl

# Location of the file
path = 'C:/Users/melikyan.tatevik/Desktop\megafeed_test_app/Soccer.xlsx'

# To open the workbook
wb = openpyxl.load_workbook(path)

# Get workbook active sheet
sheet = wb.active

# Rows to lists
row_list = [row for row in sheet.values]
# print(row_list)

list_of_lists = [list(elem) for elem in row_list]
print(list_of_lists)

for item in list_of_lists:
    if item[3] == None:
        item[3] = ''
    # elif item[3] == [1,2]:

for item in list_of_lists:
    if item[4] == None:
        item[4] = ''
