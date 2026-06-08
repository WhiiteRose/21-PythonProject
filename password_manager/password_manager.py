master_pwd = input("What is the master password ? ")


def view():
    with open('./password_manager/passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, (""))
            

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    with open('./password_manager/passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + '\n')


while True:
    mode = input("Would you like to add a new password or view existing ones ? (view, add or q to quit) ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalide mode.")
        continue