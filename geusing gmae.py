import random

store_number=0
list1=[]
def select_number():
    global  list1
    while True:
        starting_number = input("Enter your number which is started number : ").strip()
        stoping_number = input("Enter your number which is stop number : ").strip()

        if starting_number.isdigit() and stoping_number.isdigit():
            starting_number=int(starting_number)
            stoping_number=int(stoping_number)
            if starting_number < stoping_number:
                list1 = [x for x in range(starting_number, stoping_number)]
                print("List created:", list1)
                break
            else:
                print(" Starting number must be smaller than stopping number.")

        elif starting_number.isalpha() and stoping_number.isalpha():
            print("your need to enter number not Alphabit")
        elif starting_number.isdigit() and stoping_number.isalpha():
            print("your need to enter number not Alphabit : ",starting_number ," end number : ",stoping_number)
        elif starting_number.isalpha() and stoping_number.isdigit():
            print("your need to enter number not Alphabit : ",starting_number ," end number : ",stoping_number)
        else:
            print("you need to enter start ,ending number ")


def computer_select_no():
    global store_number
    global list1
    store_number=random.choice(list1)
    return store_number


def User_select_no():
    global store_number
    while True:
        user=input("Enter guessing number : ")
        if user.isdigit():
            user=int(user)
            if user==store_number:
                print("Congrudulation Your guessing is correct : " ,user ,"= computer number ", store_number)
                break
            elif user > store_number:
             print("You need to enter less number : ", user)
            elif user < store_number:
             print("You need to enter greater number : ", user)
        elif user.isalpha():
            print("your need to enter number not alphabit")

        else:
            print("your try to Enter wrong wrong alpabit")



select_number()
computer_select_no()
User_select_no()










