import openpyxl
from PIL import Image, ImageDraw
from openpyxl import Workbook
from openpyxl.styles import PatternFill
import numpy as np
from openpyxl.utils import get_column_letter, column_index_from_string

wb = Workbook()
ws = wb.active
ws1 = wb.create_sheet("Mysheet")
g = 0

for j in range(1, 100):
    for i in range(1, 100):
        g += 1
        letter = get_column_letter(g)
        ws.column_dimensions[f'{letter}'].width = 3
        ws.cell(row=j, column=i).fill = PatternFill(start_color='FF91D2FF', end_color='FF91D2FF', fill_type="solid")
wb.save('pixel_art.xlsx')

input("Press Enter to continue...")

im = Image.new('RGB', (100, 100), (255, 255, 255))
draw = ImageDraw.Draw(im)

workbook = openpyxl.load_workbook('/home/blesk/GitHub/Python_projects/pixel_art.xlsx')
sheets_list = workbook.sheetnames
sheet_active = workbook[sheets_list[0]]
x = 0
y = 0
for number in range(1, 100):
    cell_letter = get_column_letter(number)
    x += 1
    y = 0
    for cell_number in range(1, 100):
        cell_fill = sheet_active[f'{cell_letter}{cell_number}'].fill.start_color.index #Получаем цвет ячейки
        cell_hex ='#' + cell_fill[2:8]
        draw.rectangle((x-1, y, x-1, y), fill=f'{cell_hex}')
        y += 1
im.show()