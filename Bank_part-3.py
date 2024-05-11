from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rezan:rezan@cluster0.g4aqwe2.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

record = MongoClient(uri).uniqtech.Bank
branch = MongoClient(uri).uniqtech.Branch
rec = MongoClient(uri).uniqtech.Staff


class customerlogin:
    def __init__(self):
        self.userid = input("Enter the Account Number: ")
        if len(self.userid)==10 and self.userid.isdigit():
            self.pin = input("Enter the Four Digit Pin: ")
            if len(self.pin)==4 and self.pin.isdigit():
                staff1=record.find_one({"_id":self.userid})
                validate1 = {'_id':staff1["_id"],"pin":staff1["pin"]}
                validate = {"_id":self.userid,"pin":self.pin}
                if validate == validate1:
                    print('Successfully Logged-In')
                    functions = [
                           "1.Deposit",
                            "2.Withdraw",
                            "3.Check Balance"
                            ]
                    for i in functions:
                        print(i)
                    user_input = input("Which one you want to do SELECT the number (1-3): ")
                    if user_input == '1':
                        self.deposit()
                    elif user_input == '2':
                        self.withdraw()
                    elif user_input == '3':
                        self.balance()
                    else:
                        print("Invalid input. Please enter a number between 1 and 3.")
                else:
                    print("Enter the correct crendetials!!!")
                    self.__init__()
            else:
                print('Please Enter the correct pin')
                self.__init__()
        else:
            print('Please Enter the correct Account-Number !!!')
            self.__init__()
    def withdraw(self):
        amount = int(input("Enter Money want to Withdraw: "))
        if amount<=50000:
            data1 = record.find_one({"_id":self.userid,"pin":self.pin})
            data2 = data1['amount'] - amount
            data3 = {"$set":{"amount":data2}}
            record.update_one(data1,data3)
            print(f'Successfully {amount} is Debited' )
        else:
            print('error,Please Withdraw below 50,000')
    def deposit(self):
        amount = int(input("Enter Money want to Deposit: "))
        if amount<=10000000:
            data1 = record.find_one({"_id":self.userid,"pin":self.pin})
            data2 = data1['amount'] + amount
            data3 = {"$set":{"amount":data2}}
            record.update_one(data1,data3)
            print(f'Successfully {amount} is Debited' )
        else:
            print('error')
    def balance(self):
        data1 = record.find_one({"_id":self.userid,"pin":self.pin})
        data2 = data1['amount']
        print(f'Your Balance is {data2}')

class custmercreate(customerlogin):
    def __init__(self):
        username=input("Enter Custmer Name: ")
        Aadharno=(input("Enter Custmer Aadhar No: "))
        Accountno=(input("Enter Mobile (or) Account No: "))
        if(len(Accountno)==10 and Accountno.isdigit()):
            pin=(input("Create your Four Digit Pin: "))
            if(len(pin)==4 and pin.isdigit()):
                print("successfully created !!!")
                print("Please Login Below with Your Credentials ⬇️ ")
            else:
                print("Please check entered pin !")
        else:
            print("Please check account no ")

        data = {'_id':Accountno,
                'Name':username,
                'Aadharno':Aadharno,
                'pin':pin,
                'amount':0
            }
        record.insert_one(data)
        super().__init__()
        
    
class staff(custmercreate,customerlogin):
    def __init__(self):
        userid = int(input("Enter the staff-ID: "))
        self.userid = str(userid)
        if len(self.userid)==10 and self.userid.isdigit():
            pin = int(input("Enter the six Digit Pin: "))
            self.pin = str(pin)
            if len(self.pin)==6 and self.pin.isdigit():
                staff1=rec.find_one({"_id":userid})
                validate = {"_id":userid,"pin":pin}
                if staff1 == validate:
                    print('Successfully Logged-In')
                    a = [
                        "1.Create Customer Account",
                        "2.Login"
                        ]
                    for i in a:
                        print(i)
                    user = input('Which one you want to do SELECT the number 1 or 2: ')
                    if user == '1':
                        super().__init__()
                    elif user == '2':
                        customerlogin.__init__()
                    else:
                        print("Invalid input. Please enter a number 1 or 2.")
                else:
                    print("Enter the correct crendetials!!!")
                    self.__init__()
            else:
                print('Please Enter the correct pin')
                self.__init__()
        else:
            print('Please Enter the correct Staff-ID !!!')
            self.__init__()
class Bank(staff):
    def __init__(self):
        Branch=int(input("Enter yor Branch ID:"))
        Branch1=branch.find_one({"_id":Branch})
        self.Branch2 = Branch1['_id']
        self.Branch3 = Branch1['Branch']
        if(Branch==self.Branch2):
            print("successfully logged-in")
            print(f'🙏🙏Welcome to City Union Bank {self.Branch3} Branch🙏🙏')
            super().__init__()
        else:
            print("Please Check the branch ID !!!")
            self.__init__()

class main:
    a = [
        "1.Staff Login",
        "2.Customer Login"
        ]
    for i in a:
        print(i)
    user = input('Which one you want to do SELECT the number 1 or 2: ')
    if user == '1':
        Bank()
    elif user == '2':
        customerlogin()
    else:
        print("Invalid input. Please enter a number 1 or 2.")

main()





            



            

        


