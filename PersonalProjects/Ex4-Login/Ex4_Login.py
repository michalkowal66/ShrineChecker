
with open('data.txt','r') as imp:
    datafile = imp.read(1)
    if not datafile:
        data = {'id': [], 
                'pw': []}
    else:
        data = eval(imp.read())


class Logowanie:

    def check(self):
        if userID in data["id"]:
            return True
        else:
            return False

    def create(self): 
        print("User ID wasn't found in database.")
        data['id'].append(userID)
        new_password = input("Provide your new password: ")
        print(new_password,"is your new password, use it to log in")
        data['pw'].append(new_password)

    def login(self):
        for i in range(3):
            password = input("Password: ")
            if password in data['pw']:
                data['pw'].index(password) == data['id'].index(userID)
                print("Congratulations, you have logged in succesfully!")
                return True
                break
            else:
                print("Wrong password! You have",2-i,"tries left")

inst = Logowanie()

userID = str(input("Provide existing or new user ID: ")) 
while True:
    inst.check()
    if inst.check():
        inst.login()
        break
    else:
        inst.create()

f = open("data.txt","w")
f.write( str(data) )
f.close()