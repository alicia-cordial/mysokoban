import mysql.connector

class Database:

    def __init__(self) -> None:
        pass

    def insertScoreDatabase(self, player,timescore):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mysokoban"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO score (player, timescore) VALUES (%s, %s)"
        val = (player, timescore)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        mydb.close()
        
