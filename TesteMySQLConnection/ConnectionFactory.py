import mysql.connector

try:
    con=mysql.connector.Connect(user="user", password="password", host="localhost", database="database")
except:
    print("não foi possivel conectar ao banco de dados")

class ConnectionFactory():


    def listar(self,sql,val):
        con._open_connection()
        mycursor=con.cursor()
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        con.close()

    def executar(self,sql,val):
        con._open_connection()
        mycursor=con.cursor()
        mycursor.execute(sql,val)
        con.commit()

    def listartodos(self):
        con._open_connection()
        mycursor=con.cursor()
        mycursor.execute("select * from pessoa")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        con.close()

