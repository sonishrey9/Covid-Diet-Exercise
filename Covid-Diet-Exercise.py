# covid diet & exercise management system

from datetime import datetime as d


def time_and_date():  # function o take time and date input from user

    date = d.now()

    return date.strftime("%d-%m-%Y , %H:%M:%S")


# time_and_date()
user_list = ["shrey1", "shrey" , "hanuman"]
print("Client list is", user_list)

def hms():
    """this is function of health management system for maintaining diets and exercise"""

    while (1):

        print("Enter number  of the client \n"
              "1. shrey1 : \n"
              "2. shrey : \n"
              "3. hanuman : \n"
              "4. Type 'New user' To open a new account")
        c_num = input()

        if (c_num == 1 or c_num == "shrey1"):

            print(("welcome to shrey1 diet and exercise file").upper())
            time_and_date()
            # a=time_and_date()
            # print(a)
            detail_num = input("enter detail value you want to enter, 1. for diet , 2. for exercise")

            if (detail_num == "1" or detail_num == "diet"):
                with open("harrydiet.csv", "a+") as sd1:
                    details = input("enter the deatils \n")
                    sd1.write(f" {time_and_date()} {details} \n")
                    f" {time_and_date()} {details} \n"


            elif (detail_num == "2" or detail_num == "exercise"):
                with open("harryexercise.csv", "a+") as se1:
                    details1 = input("enter the deatils \n")
                    se1.write(f" {time_and_date()} {details1} \n")
                    print(f" {time_and_date()} {details1} \n")


            else:
                print("invalid choice")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or "y":
                continue

            else:
                break


        elif (c_num == "2" or c_num == "shrey"):

            print(("welcome to shrey diet and exercise file").upper())
            time_and_date()
            detail_num = input("enter detail value you want to enter, 1. for diet , 2. for exercise")

            if (detail_num == "1" or detail_num == "diet"):
                with open("shreydiet.csv", "a+") as sd:
                    details = input("enter the deatils \n")
                    sd.write(f"{time_and_date()} {details} \n ")
                    print(f" {time_and_date()} {details} \n")


            elif (detail_num == "2" or detail_num == "exercise"):
                with open("shreyexercise.csv", "a+") as se:
                    details1 = input("enter the deatils \n")
                    se.write(f" {time_and_date()} {details1} \n")
                    print(f" {time_and_date()} {details1} \n")


            else:
                print("invalid choice")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or answer == "y":
                continue

            else:
                break

        elif (c_num == "3" or c_num == "Hanuman"):

            print(("welcome to hanuman diet and exercise file").upper())
            time_and_date()
            detail_num = input("enter detail value you want to enter, 1. for diet , 2. for exercise")

            if (detail_num == "1" or detail_num == "diet"):
                with open("hanumandiet.csv", "a+") as had:
                    details = input("enter the deatils \n")
                    had.write(f" {time_and_date()} {details} \n")
                    print(f" {time_and_date()} {details} \n")


            elif (detail_num == "2" or detail_num == "exercise"):
                with open("hanumanexercise.csv", "a+") as hae:
                    details1 = input("enter the deatils \n")
                    hae.write(f" {time_and_date()} {details1} \n")
                    print(f" {time_and_date()} {details1} \n")


            else:
                print("invalid choice")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or answer == "y":
                continue

            else:
                break


        elif (c_num == "4" or c_num == "New user"):
            user = input("enter user name")
            user_list.append(user)
            file_type = input("enter file you want to create \n"
                              "1. Diet \n"
                              "2. Exercise")

            if file_type == "1" or file_type == "diet":
                with open(f" {user}.csv", "a+") as user_diet:
                    details = input("enter the deatils \n")
                    user_diet.write(f" {time_and_date()} {details} \n")
                    print(f" {time_and_date()} {details} \n")

            elif file_type == "2" or file_type == "exercise":
                with open(f" {user}.csv", "a+") as user_exercise:
                    details = input("enter the deatils \n")
                    user_exercise.write(f" {time_and_date()} {details} \n")
                    print(f" {time_and_date()} {details} \n")

            else:

                print("invalid choice")

            answer = input("Do you Wish to continue, Type Y for yes, N for No")

            if answer == "Y" or answer == "y":
                continue

            else:
                break


        else:
            print("invalid choice")

        answer = input("Do you Wish to continue, Type Y for yes, N for No ")

        if answer == "Y" or answer == "y":
            continue

        else:
            break


hms()

