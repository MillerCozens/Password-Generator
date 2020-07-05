import random
g_password = ""
g_score = 0

def password_generator():
    global g_password
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890$%^&*()!"
    print ("How many character do you wont in your password: ")
    length = int(input())
    password = ""
    for i in range(length):
        index = random.randrange(len(chars))
        password = password + chars[index]
    print (password)
    g_password = password
    getmenuoptions()

def password_checker(p):
    global g_score
    if len(p) >=6 and len(p) <= 12:
        print("your password is in the range. your password has gained 20 points")
        g_score = g_score + 20
        print (g_score)
    
    if p.lower()== p or p.upper()==p or p.isalnum()==p:
        print ("your password is weak")
        g_score = g_score + 10
    elif p.lower()== p and p.upper()==p or p.isalnum()==p:
        print ("tour passwor dis meduim strength")
        g_score = g_score + 15
    else:
        p.lower()== p and p.upper()==p and p.isalnum()==p
        print ("your password is strong")
        g_score = g_score + 15
        print (g_score)
        g_score = 0
        
    return getmenuoptions()
    
    
def getmenuoptions():
    print()
    
    choice = input("""
    -----Menu-----
    Please Choose an Option: 
    A: password_generator
    B: password_checker
    C: Quit
    - Weak password = 10
    - Meduim password = 20
    - Strong password = 30+

---> """)

    if choice == 'A' or choice == 'a':
        password_generator()
        
    elif choice == 'B' or choice == 'b':
        password_checker(g_password)
    elif choice == 'C' or choice == 'c':
        print("You have exited the menu")
    else:
        print("You didn't select an option")
        print("Please try again")
        getmenuoptions()


getmenuoptions()
        
