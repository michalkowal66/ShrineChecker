import json
import collections
import time

data = json.load(open("data.txt"))
tries = json.load(open("tries.txt"))
block = json.load(open("block.txt"))
tstamps = json.load(open("tstamps.txt"))


def trylog(i = 0):
    while i < 3:
        userID = input("Username: ")
        if userID in block:
            blocked(userID)
            break
        elif len(userID) <= 3:
            print("The username must be at least 4 characters long!")
            i == 0
            continue
        elif userID not in data["id"]:
            print("User ID wasn't found in database.\n Create an account to log in.")
            break

        password = input("Password: ")
        if password in data['pw'] and data['pw'].index(password) == data['id'].index(userID):
            print("Congratulations, you have logged in succesfully!")
            while userID in tries:
                tries.remove(userID)
            enter = True
        else:
            if tries.count(userID) >= 2:
                block.append(userID)
                t = int(time.time())
                tstamps['id'].append(userID)
                tstamps['rtime'].append(t + 900)
                break
            else:
                i = tries.count(userID)
                print("Wrong password! You have",2-i,"tries left.")
                tries.append(userID)
                enter = False

            
        if enter:
            print(userID,password)
            logged(userID)
            break

       

def check(i = 0):
    while i < 3:
        userID = input("Provide your username: ")
        if len(userID) <= 3:
            print("The username must be at least 4 characters long!")
            i += 1
        else:
            if userID in data["id"]:
                print("User ID was found in database. Log in from main menu using option '1'.")
                break
            else:
                print("User ID wasn't found in database. Proceeding to account creator.")
                create(userID)
                break

def create(new_id): 
    for i in range(3):
        new_password = input("New password: ")
        new_password2 = input("Repeat password: ")
        if new_password == new_password2:
            data['id'].append(new_id)
            print("Passwords match,",new_password,"is your new password, use it to log in")
            data['pw'].append(new_password)
            break
        elif i < 2:
            print("Passwords do not match!",2-i,"tries left.")
        elif i == 2:
            print("No tries left.")

def logged(id):
    loggeddec = input("Press (key) if you want to: \n- (1)logout\n- (2)remove your account\n>>>")
    if loggeddec == "1":
        return
    elif loggeddec == "2":
        if deluser(id):
            return  

def blocked(id):
    now = time.time()
    userIndex = tstamps['id'].index(id)
    if now <= tstamps['rtime'][userIndex]:
        remaining = int(tstamps['rtime'][userIndex]-now)
        print("Account blocked. Remaining time:",remaining,"seconds.")
    else:
        while id in tries:
            tries.remove(id)
        block.remove(id)
        tstamps['id'].pop(userIndex)
        tstamps['rtime'].pop(userIndex)
        print("Login system unlocked!")


def deluser(id):
    deldec = input("Are you sure, you want to delete your account?\n>>>")
    if deldec == "y":
        userIndex = data['id'].index(id)
        confirm = input("Provide password to your account to confirm your decision\n>>>")
        if confirm == data["pw"][userIndex]:
            data["id"].pop(userIndex)
            data["pw"].pop(userIndex)
            return True
        else:
            print("Wrong password.")
            
    elif deldec == "n":
        return False

def mainMenu():
    while True:
        dec = input("You are in main menu. Choose action:\n 1 - log in\n 2 - create an account\n 3 - quit\n>>>")
        if dec == "1":
            trylog()  
        elif dec == "2":
            check()
        elif dec == "3":
            print("Goodbye!")
            break

mainMenu()

json.dump(data, open("data.txt",'w'))
json.dump(tries, open("tries.txt",'w'))
json.dump(block, open("block.txt",'w'))
json.dump(tstamps, open("tstamps.txt", 'w'))

print("test")