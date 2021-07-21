import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='Manny', passwd='Manny@Nf201', port='3306', database='fakeatm')
mycursor = mydb.cursor()


#
# mycursor.execute('SELECT * FROM Accounts')
# Accounts = mycursor.fetchall()

# for account in Accounts:
#     print(account)
#     print('Account Number: ' + str(account[0]))
#     print('Pin: ' + str(account[1]))
#     print('Account Name: ' + str(account[2]))
#     print('Balance R: ' + str(account[3]))

def CreateAcc():
    accNum = int(input("Enter Account Number (10 digit account Number): "))
    pin = int(input("Enter pin (4 digit pin): "))
    accName = input("Enter Account Name: ")
    balance = int(input("Enter new balance: "))
    data1 = (accNum, pin, accName, balance)
    sql1 = "insert into Accounts values (%s, %s, %s, %s)"
    mycursor.execute(sql1, data1)
    mydb.commit()
    print("Account Created")


def login():
    trail = 3
    attempt = 0
    while True:
        accnum = input("Please enter Account number: ")
        pin = input("Please enter pin: ")
        data = (accnum, pin)
        find_user = "SELECT * FROM Accounts WHERE accNum = %s AND pin = %s"
        mycursor.execute(find_user, data)
        acc = mycursor.fetchall()

        if acc:
            for i in acc:
                print("Welcome" + i[2])
                print('''Main Menu
                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Transfer
                5. Go back''')
                choice = int(input("Please select an option: "))

                if choice == 1:
                    print("Account Number" + str(i[0]))
                    print("Balance: R" + str(i[3]))
                    break

                elif choice == 2:
                    amount = float(input("Please enter the amount being deposit: "))
                    newBalance = amount + float(i[3])
                    print("New Balance: R" + str(newBalance))
                    info = (int(newBalance), i[0])
                    newB = "UPDATE Accounts SET balance = %s WHERE accNum = %s"
                    try:
                        mycursor.execute(newB, info)
                        mydb.commit()
                        print("balacne successfully updated")
                    except:
                        print("error could not update")
                    break

                elif choice == 3:
                    amount = float(input("Please enter the amount being withdraw: "))
                    newBalance = float(i[3]) - amount
                    print("New Balance: R" + str(newBalance))
                    info = (int(newBalance), i[0])
                    newB = "update Accounts set balance = %s where accNum = %s"
                    try:
                        mycursor.execute(newB, info)
                        mydb.commit()
                        print("balacne successfully updated")
                    except:
                        print("error could not update")
                    break

                elif choice == 4:
                    acc = int(input("Please enter account you would like to send money to: "))
                    amount = float(input("Please Enter amoun being transfered"))
                    newBalance = float(i[3]) - amount
                    print("New Balance: R" + str(newBalance))
                    info = (int(newBalance), i[0])
                    newB = "update Accounts set balance = %s where accNum = %s"
                    try:
                        mycursor.execute(newB, info)
                        mydb.commit()
                        print("balacne successfully updated")
                    except:
                        print("error could not update")
                    break


                elif choice == 5:
                    print("Going back to menu")
                    menu()
                    break

                else:
                    print("Invaid input")
                break
        else:
            print("Incorrect Account Number or pin")
            attempt += 1
            if attempt == trail:
                print("To many invaild input")
        break


def menu():
    print('''
    1. Create New Account
    2. Login
    3. exit''')
    choice = int(input("Please slecet an option: "))
    if choice == 1:
        CreateAcc()
    elif choice == 2:
        login()
    elif choice == 3:
        print("GoodBye")
    else:
        print("Invalid option")
        menu()


menu()
