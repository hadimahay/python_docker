import mysql.connector


menu = '''1-show blog.\n
2-create blog.\n
3-delete blog.\n
4-edit blog.\n
5-exit\n\n'''


def connect():
    mydb = mysql.connector.connect(
                                    host="mysql",
                                    user="root",
                                    password="",
                                    database="blog"
)
    return mydb

def fetch(mydb):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM blog")

    myresult = mycursor.fetchall()

    return myresult

def show(myresult):
    
    for blog in myresult:
        Blog = f'''title: {blog[0]}.\n body : {blog[1]}.\n\n'''
        print(Blog) 

def create(mydb, title, body):

    mycursor = mydb.cursor()

    v = '''INSERT IGNORE INTO blog(title,body) VALUES(%s,%s)'''
    s = (title , body)

    mycursor.execute(v,s)
  
    mydb.commit()

    print ('your blog has been added\n\n')


def delete(mydb,title):
    mycursor = mydb.cursor()

    sql = f"DELETE FROM blog WHERE title = {title}"

    mycursor.execute(sql)

    mydb.commit()

    print ('the blog in question has been delete\n\n')

def edit(mydb , title , new_title , new_body):
    mycursor = mydb.cursor()

    edit_title = f"UPDATE blog SET title = {new_title} WHERE title = {title}"
    edit_body  = f"UPDATE blog SET blod = {new_body} WHERE title = {title}"
    mycursor.execute(edit_body)
    mycursor.execute(edit_title)

    mydb.commit()
    print ("update done\n\n")


if __name__ == "__main__":

    
    while True:
        mydb = connect()
        myresult = fetch(mydb)
        print (menu)
        
        num = int(input("enter number: "))

        if num == 1:
            show(myresult)

        elif num == 2:
            title = str(input("enter title :"))
            body  = str(input("enter body: "))

            create(mydb,title,body)

        elif num == 3:
            title = str(input("enter title :"))

            delete(mydb,title)

        elif num == 4:
            title     = str(input("enter title :"))
            new_title = str(input("enter new title :"))
            new_body  = str(input("enter new  body :"))

            edit(mydb,title,new_title,new_body)

        elif num == 5:
            break

        else:
            print ("your number out of range list\n\n")