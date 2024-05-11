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
                    check: str = input("Are you sure? (y/n): ")
                    if check.lower() == "y":
                        DBController.insertData(service, mail, login, pwd)
                    else:
                        continue
                case 3:
                    print("Edit")
                    print("1. service | 2. mail | 3. login | 4. pwd")
                    dataToChange: int = inputConverter(input("Enter which data is to change: "))
                    if dataToChange < 1 or dataToChange > 4:
                        print("Data out of range!")
                        continue
                    itemID: int = int(input("Item ID: "))
                    newData: str = input("Enter new data: ")
                    check: str = input("Are you sure? (y/n): ")
                    if check.lower() == "y":
                        DBController.updateData(newData, itemID, dataToChange)
                    else:
                        continue
                case 4:
                    print("Delete")
                    itemID: int = inputConverter(input("ID: "))
                    check: str = input("Are you sure? (y/n): ")
                    if check.lower() == "y":
                        DBController.deleteData(itemID)
                    else:
                        continue
                case 0:
                    print("Exiting...")
                    break
                case None:
                    input("Consider using numeric values. Press Enter to continue...").rstrip()
                case _:
                    input("Input out of range. Press Enter to continue...").rstrip()
