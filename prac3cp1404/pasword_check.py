def main():
    password = input("Enter password:")
    newpassword = get_password(password)
    print(newpassword)

def get_password(password):
    newpassword = ""
    for x in range(len(password)):
        newpassword = newpassword + "*"
    return newpassword
main()