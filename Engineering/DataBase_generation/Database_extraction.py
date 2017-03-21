'''
Created on 6Nov.,2016

@author: Nath
'''
import sqlite3
import xlsxwriter
conn = sqlite3.connect('my_first_db1.db3')

c = conn.cursor()

string1 = c.execute('select * from table1 where column1 = 80000')

workbook = xlsxwriter.workbook('sqlitetable.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(string1)

workbook.close()

 
