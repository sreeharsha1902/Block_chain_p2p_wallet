import json
import datetime
import BC
import ZKP
import time
#Global Variables
accounts = []
#u1 = 5 -> 10
#u2 = 7 -> 7
#u3 = 9 ->6


def SaveUserAccounts(accounts):
    userdata = {}
    i =1
    for a in accounts:
        userdata[i] = a
        i = i+1
    with open('UserData.txt', 'w') as outfile:
            json.dump(userdata,outfile )

def LoadUserAccounts():
    accounts = []
    with open('UserData.txt', 'r') as infile:
        userdata = json.load(infile)

    for v in userdata.values():
        accounts.append(v)
    
    #print(accounts)
    return accounts 
def add_user(Account_ID, Bal,accounts, Y):
    user = {"Account_ID":Account_ID,"Balance" : Bal, "Y":Y }
    #accounts = LoadUserAccounts
    accounts.append(user)
    SaveUserAccounts(accounts)
    print("New User Added ")
    return True

    return
def show_options(accounts,bc):
    print("OPTIONS")
    print("1. Make a transaction")
    print("2. View user transactions")
    print("3. Verify Block Chain")
    print("4. Add User")
    print("5. Show all user data")
    print("6. Display BlockChain")
    print("Select an option : ", end ="")
    option = ( input())
    option = int(option)
    print()
    
    if(option  in [1,2,3,4,5,6]):
        handle_options(option,accounts,bc)
        return
    else :
        print("Invalid Option! ")
        return
    
    return



def make_transaction(accounts,SAN,RAN,amount):
    for a in accounts:
        if(a['Account_ID'] == RAN):
            a['Balance'] += amount
        if(a["Account_ID"] == SAN):
            a['Balance'] -= amount
    SaveUserAccounts(accounts)
    return True
        
    
def print_receipt(Receipt):
    print('Sender Account ID : ' + str(Receipt['Sender Account ID']))   
    print('Recipient Account ID : ' + str(Receipt['Recipient Account ID']))
    print('Amount transferred : ' + str(Receipt['Amount transferred']))
    print('Transaction time : ' + str(Receipt['Transaction time']))  

    return

def authenticate_user_(accounts,SAN):
    for a in accounts:
        if(a["Account_ID"] == SAN):
            return ZKP.authenticate_user(a["Y"])


def handle_options(option,accounts,bc):
    if option is 1:

        #Input Sender & recipient account number and ammount
        SAN = input("Enter sender Account number : ")
        RAN = input("Enter recipient Account number : ")
        amount =int(input("Enter amount to transfer : "))
        if(amount <=0):
            print("Invalid amount value !")
            return
        
        #Verify Account details
        print("Verifying account details and balance ...")
        b = verify_account_details(SAN,RAN,amount,accounts)
        if(b):
            print("Account details verified")
        else:
            print("Account details verification failed !")
            return 

        #Authenticate User using ZKP
        print("Authenticating user ...")

        b= authenticate_user_(accounts,SAN)
       # print('b is' + str(b))
        if( b):
            print("Authentication complete")
            
        else:
            print("Authentication failed !")
            return
       


        


        #Make Data object
        print("Creating a transaction receipt ...")
        Receipt = {}
        Receipt['Sender Account ID'] = SAN
        Receipt['Recipient Account ID'] = RAN
        Receipt['Amount transferred'] = amount
        Receipt['Transaction time'] = str(datetime.datetime.now())
        print_receipt(Receipt)



        #Mine Block
        print("Saving transaction to blockchain ...")
        b = bc.mine_block(Receipt)
        if(b):
            print("Transaction saved to blockchain")
        else:
            print("Saving transaction to blockchain failed !")
            return
        
        #Make Transaction
        print("Transferring amount ...")
        b = make_transaction(accounts,SAN,RAN,amount)
        if(b):
            print("Amount transfer success ")
        else:
            print("Amount transfer failed !")
            return 


        return

    elif option is 2:
        #View all user transactions
        #Enter your Account number
        AN = input("Enter your Account number : ")
        for a in accounts:
            if(a['Account_ID'] == AN):
        #print("You Entered : " + str(AN))
                print("Showing all transactions against account ID : " + str(AN))
                view_User_transactions(AN,bc)
                return
           
        print("Invalid account ID !")
        return
        
        

    elif option is 3:
        #Verify Block Chain_
        print("Verifying Block Chain .....")
        b = bc.valid()

        
        return
    elif option is 4:
        Account_ID = input("Enter a new Account ID :")
        Bal = int(input("Enter account balance : "))
        Y = int(input("Enter Y = (g^x)%p : "))
        add_user(Account_ID,Bal,accounts,Y )
        return
    elif option is 5:
        print_users(accounts)
        return
    
    elif option is 6:
        bc.Print_Block_Chain()
        return
         
    else:
        print('Unkown Option Selected')
        return

    
def verify_account_details(SAN,RAN,Amount,accounts):
    b_SAN = False
    b_RAN = False
    b_Bal = False

    #print(accounts)
    for a in accounts:
        if(a['Account_ID'] == RAN):
            b_RAN = True
        if(a["Account_ID"] == SAN):
            b_SAN = True
            if int(a['Balance']) >= Amount:
                b_Bal = True
        
        
    if b_SAN is False:
        print("Sender Account not found !")
    elif b_Bal is False:
        print("Insufficient funds in senders account !")
    if b_RAN is False:
        print("Recipient Account not found !")
    

    return b_Bal*b_SAN*b_RAN

def print_users(accounts):
    print("Current User Data : ")
    #print(accounts)
    for a in accounts:
        print(a['Account_ID'] + "  " + str(a['Balance']))


def view_User_transactions(Account_ID,bc):
    
    for b in bc.Chain_:
        if( (b['data']['Sender Account ID'] == str(Account_ID)) or( b['data']['Recipient Account ID'] == str(Account_ID ))):
            data = b['data']
            print('Transferred ' + str(data['Amount transferred']) + " from " + str(data['Sender Account ID']) +" to " +  str(data['Recipient Account ID']) )


def main_function():
    #Load all user data
    accounts = LoadUserAccounts()
    bc = BC.Blockchain()
    #print(accounts)
    #print_users(accounts)
    show_options(accounts,bc)



'''   
main_function()
'''
while True:
    try:
        main_function()
    except:
        #break
        print(" An unexpected error occurred! Reloading page ....")
        time.sleep(1.5)
        print()
        print("------------------------------------------------------------")
        continue
    print()
    print("------------------------------------------------------------")
#accounts = LoadUserAccounts()
#print_users()
