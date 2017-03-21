'''
Created on 6Nov.,2016

@author: Nath
'''
def making_an_sqlite_db():
    import sqlite3
    
    sqlite_file = 'my_first_db1.sqlite' ##name of the database to be created##
    table_name1 = 'my_table_1' #name of first table to be created#
    table_name2 = 'my_table_2' #name of second table to be created#
    
    new_field = 'my_first_column' #name of first column to be created#
    
    field_type = 'INTEGER' #type of data the column will contain#
    
    
    #connecting to the database file#
    conn = sqlite3.connect(sqlite_file)
    
    c = conn.cursor()
    
    #Creating a new sqlite table with 1 column
    c.execute('CREATE TABLE {tn} ({nf} {ft})'\
              .format(tn = table_name1, nf = new_field, ft = field_type))
    
    #creating second table with 1 column and set it as Primary Key
    #note primary key columns can only consist of unique values
    
    c.execute('CREATE TABLE {tn} ({nf} {ft})'\
              .format(tn = table_name2, nf = new_field, ft = field_type))
    
    #committing changes and closing the connection to the database file
    
    conn.commit
    conn.close


