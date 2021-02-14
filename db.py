import sqlite3 as sq



def switcher(i):
    
        switch = { 
                1 : '''select name from project AS p , (select * from salary AS s,
                        projectSalary AS p where currency='Ripple' and s.salaryID =
                        p.salaryID) AS temp where p.pID = temp.pID;''',
                2 : "select name,max(expenses) from project;",
                3 : """select name from project where startDate >= '2020-01-01' """,
                4 : """select name from project""",
                5 : "select email from user where location='Tehran'",
                6 : """select description from goal""",
                7 : """select name from project where pID IN
                        (select pID from do where userID =
                        (select userID from user where name = 'Ashkan'))""",
                9 : """select paymentMethod from salary where salaryID IN
                        (select salaryID from projectSalary where pID IN
                        (select pID from project where customerID IN
                        (select customerID from customer where
                        customerName = 'PartSoftwareGroup')))""",
                8 : """select paymentMethod from salary where salaryID IN
                       (select salaryID from projectSalary where pID IN
                        (select pID from project where pID IN
                        (select pID FROM do where userID = (select userID from user where
                        name like '%Arash Kariznovi%'))));""",
                10:  """select description from goal where userID =
                        (select userID from user where name like '%Susan kazemi%');""",
        }
        return switch.get(i)

    
def insertVaribleIntoTable(id, email, name, location, DateofBirth):
    
        try:
                conn = sq.connect('ProjectManager.db')
                cursor = conn.cursor()
                cursor.execute('PRAGMA foreign_keys = ON')
                sqlite_insert_with_param = """INSERT INTO user
                        (userID, email, name, location, DateOfBrith)
                         VALUES (?, ?, ?, ?, ?);"""

                data_tuple =(id, email, name, location, DateofBirth)
                cursor.execute(sqlite_insert_with_param, data_tuple)
                conn.commit()
                print("Python Variables inserted successfully into user table")

                cursor.close()

        except sq.Error as error:
                print("Failed to insert Python variable into sqlite table", error)
               
        finally:
                if (conn):
                        conn.close()
                        print("the sqlite connection is closed")
                        
def deleteRecord(id):
        
    try:
        conn = sq.connect('ProjectManager.db')
        cursor = conn.cursor()   
        sql_delete_query = """DELETE from user where userID = %d""" %(id)
        cursor.execute(sql_delete_query)
        conn.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sq.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("the sqlite connection is closed")

def updateSqliteTable(nam,prenam):
    try:
        conn = sq.connect('ProjectManager.db')
        
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        print("Connected to SQLite")
        
        sql_update_query = """Update user set name = '%s' where name = '%s' """ %(nam,prenam)
        cursor.execute(sql_update_query)
        conn.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sq.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (conn):
            conn.close()
            print("The SQLite connection is closed")


                

print('Welcome to the Database Application')


print("\n Type 1 if you want to see the queries")
print("\n Type 2 to insert")
print("\n Type 3 to delete")
print("\n Type 4 to update")
        
stat = int(input())

print("Connected to SQLite")

if stat==1:
        
   conn = sq.connect('ProjectManager.db')
   c = conn.cursor() 
   while True:
        print('\nTo see the Projects which are paid by Ripple type "1"')
        print('To see the projects with the most expenses type "2"')
        print('To see the projects that starts at year 2020 type "3"')
        print('To see the projects name type "4"')
        print('To see the email of users who are from Tehran type "5"')
        print('To see the goals of users type "6"')
        print('To see the projects that "Ashkan" did type "7"')
        print('To see the methods that "Arash Kariznovi" has been paid type "8"')
        print('To see the methods of payment in "PartSoftwareGroup" type "9"')
        print('To see the goals of Ms."Susan Kazemi" type "10"')

        selection = int(input())
        i = switcher(selection)
        c.execute(i)
        query = c.fetchall()
        for i in query:
            print(i)



                
elif stat==2:
    
    print("insertVaribleIntoTable(11,'Peyman@gmail.com', 'Peyman', 'Paris', '1111-11-11')")
    insertVaribleIntoTable(11,'Peyman@gmail.com', 'Peyman', 'Paris', '1111-11-11')

elif stat==3:
        
    print("Type the user id you want to delete")    
    id=int(input())    
    deleteRecord(id)
    print("user with id %d is delete!") %id
    
elif stat==4:
      print("Type the you want to replace:")
      prename = str(input())
      print("Type new name")
      name = str(input())
      updateSqliteTable(name,prename)
    

    

