from src.inputHandler import inputConverter
from src.dbcontroller import DBController


class Menu:

    @staticmethod
    def showMenu():
        DBController.createTable()
        menuChoice: int | None = None
        while menuChoice != 0:
            print("1. Show all")
            print("2. Insert new")
            print("3. Edit")
            print("4. Delete")
            print("0. Exit")
            menuChoice = inputConverter(input("Enter your choice: "))

            match menuChoice:
                case 1:
                    DBController.showAll()
                case 2:
                    print("Insert new")
                    service: str = input("Service: ")
                    mail: str = input("Mail: ")
                    login: str = input("Login: ")
                    pwd: str = input("Current: ")
                    check: str = input("Insert data? (y/n): ")
                    if check.lower() == "y":
                        DBController.insertData(service, mail, login, pwd)
                    else:
                        break
                case 3:
                    print("2. Edit")
                case 4:
                    print("3. Delete")
                case 0:
                    print("Exiting...")
                    break
                case None:
                    input("Consider using numeric values. Press Enter to continue...").rstrip()
                case _:
                    input("Input out of range. Press Enter to continue...").rstrip()
