from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view_passwords():
    try:
        with open('credentials.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                title, userId, pwd = data.split("|")
                print("Title:", title, "\nUserId:", userId, "\nPassword:", fer.decrypt(pwd.encode()).decode())
    except ValueError:
        print("Error: Invalid data format in the file.")

            
def add_password():
    title = input("Enter Credential Title: ")
    userId = input ("Enter User ID: ")
    pwd = input("Enter Password: ")
    
    with open('credentials.txt', 'a') as f:
        f.write(title + "|" + userId + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
def create_account():
    print("Hello User! Welcome to Password Vault!")
    org_userId = input("Create a new user ID: ")
    org_pwd = input("Create a new password: ")
    with open('new_user.txt', 'a') as f:
        f.write(org_userId + "|" + fer.encrypt(org_pwd.encode()).decode() + "\n")
        
def login_account():
    log_userId = input("Please enter user ID to login: ")
    log_pwd = input("Please enter password to login: ")
    try:
        with open('new_user.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                org_userId, org_pwd = data.split("|")
                org_pwd = fer.decrypt(org_pwd.encode()).decode()
    except ValueError:
        print("Error: Invalid data format in the file.")
    while True:
        if(log_userId == org_userId and log_pwd == org_pwd):
            print("User logged in successfully!")
            print("1. Add a new password -> \n2. List out existing passwords -> \n3. Exit ->")
            mode = input("Select an option from given menu: ")
            if mode == '3':
                quit()
            elif mode == '1':
                add_password()
                break
            elif mode == '2':
                view_passwords()
                break
            else:
                print("Invalid Option.")
                break
        else:
            print("Failed to login!")
            break

def main():
    print("*-*-*-*-*-*-*-*-MENU-*-*-*-*-*-*-*-*")
    print("1. Create a new account -> \n2. Login to existing account-> \n3. Exit ->")
    mode = input("Select an option from given menu: ")
    if mode == '3':
        quit()
    elif mode == '1':
        create_account()
    elif mode == '2':
        login_account()
    else:
        print("Invalid Option.")
    
main()
