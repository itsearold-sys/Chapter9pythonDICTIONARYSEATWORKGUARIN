print("======= Record Keeping App =======")
print("a. Add Data")
print("b. Delete Data")
print("c. End")


table = dict()
table = [""]

option = input("Select action: ")

if option == "a":
    key = input("Enter a key: ")
    name = input("Enter value: ")
    print(name)

if option == "b":
    key = input("Enter a key: ")
    value = input("Enter value: ")

if option == "c":
    print("THANK YOU. Program will now end")
    exit()




