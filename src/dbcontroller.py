import sqlite3


class DBController:

    def __init__(self):
        raise NotImplemented

    @staticmethod
    def createTable() -> None:
        dbConnection = sqlite3.connect('storage.db')

        dbCursor = dbConnection.cursor()

        dbCursor.execute("""CREATE TABLE IF NOT EXISTS storage(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SERVICE TEXT,
        MAIL TEXT,
        LOGIN TEXT,
        PWD TEXT
        )""")

        dbConnection.commit()
        dbConnection.close()

    @staticmethod
    def showAll() -> None:
        dbConnection = sqlite3.connect('storage.db')
        dbCursor = dbConnection.cursor()
        dbCursor.execute("SELECT * FROM storage")
        table: list = dbCursor.fetchall()
        for row in table:
            print(f'ID: {row[0]:<3} | Service:  {row[1]:<20} | Mail: {row[2]:<20} | Login: {row[3]:<20} | Pwd: {row[4]:<20}')
        dbConnection.commit()
        dbConnection.close()

    @staticmethod
    def insertData(service: str, mail: str, login: str, current: str) -> None:
        dbConnection = sqlite3.connect('storage.db')
        dbCursor = dbConnection.cursor()

        dbCursor.execute(f"INSERT INTO storage (SERVICE, MAIL, LOGIN, PWD) VALUES ('{service}', '{mail}', '{login}', '{current}')")
        dbConnection.commit()
        dbConnection.close()

    @staticmethod
    def updateData(newData: str, itemID: int, dataToChange: int) -> None:
        dbConnection = sqlite3.connect('storage.db')
        dbCursor = dbConnection.cursor()
        if dataToChange == 1:
            dbCursor.execute(f"UPDATE storage SET SERVICE = '{newData}' WHERE ID = {itemID}")
        elif dataToChange == 2:
            dbCursor.execute(f"UPDATE storage SET MAIL = '{newData}' WHERE ID = {itemID}")
        elif dataToChange == 3:
            dbCursor.execute(f"UPDATE storage SET LOGIN = '{newData}' WHERE ID = {itemID}")
        else:
            dbCursor.execute(f"UPDATE storage SET PWD = '{newData}' WHERE ID = {itemID}")
        dbConnection.commit()
        dbConnection.close()

    @staticmethod
    def deleteData(itemID: int) -> None:
        dbConnection = sqlite3.connect('storage.db')
        dbCursor = dbConnection.cursor()
        dbCursor.execute(f"DELETE FROM storage WHERE ID = {itemID}")
        dbConnection.commit()
        dbConnection.close()

