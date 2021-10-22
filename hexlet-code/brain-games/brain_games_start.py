name=""

def get_start():
    global name
    print("Print for start >>> brain-games")
    start=input()
    while start!="brain-games":
        start=input("Print for start >>> brain-games")
        if start=="brain-games":
            print("Welcome to the Brain Games!")
            break

    print("what is your name?")
    name=input()

    while name == '':
        print("what is your name?")
        name = input()
        if name!="":
            break

    print("Hello,",name)
