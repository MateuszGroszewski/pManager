import sqlite3


class DBController:

    def __init__(self):
        raise NotImplemented

    @staticmethod
    def createTable() -> None:
        conn = sqlite3.connect('storage.db')

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS storage(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SERVICE TEXT,
        MAIL TEXT,
        LOGIN TEXT,
        PWD TEXT
        )""")

        conn.commit()
        conn.close()

    @staticmethod
    def showAll() -> None:
        conn = sqlite3.connect('storage.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM storage")
        table: list = cur.fetchall()
        for row in table:
            print(f'ID: {row[0]:<3} | Service:  {row[1]:<20} | Mail: {row[2]:<20} | Login: {row[3]:<20} | Pwd: {row[4]:<20}')
        conn.commit()
        conn.close()

    @staticmethod
    def insertData(service: str, mail: str, login: str, current: str) -> None:
        conn = sqlite3.connect('storage.db')
        cur = conn.cursor()

        cur.execute(f"INSERT INTO storage (SERVICE, MAIL, LOGIN, PWD) VALUES ('{service}', '{mail}', '{login}', '{current}')")
        conn.commit()
        conn.close()

    @staticmethod
    def updateData() -> None:
        conn = sqlite3.connect('storage.db')
        cur = conn.cursor()
        cur.execute(f"UPDATE storage SET PWD = ''")
        conn.commit()
        conn.close()

    @staticmethod
    def deleteData(service: str, mail: str, login: str) -> None:
        raise NotImplemented
