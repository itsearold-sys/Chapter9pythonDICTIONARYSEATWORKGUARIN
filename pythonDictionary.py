print("===== Record Keeping App =====")

table = {}

while True:
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    option = input("Select action: ").lower()

    if option == "a":
        key = input("Enter a key: ").upper()
        value = input("Enter value: ")

        table[key] = value
        print(table)

    elif option == "b":
        key = input("Enter a key: ").upper()

        if key in table:
            table.pop(key)
            print(table)
        else:
            print("=== Key does not exists! ===")
            continue

    elif option == "c":
        print("THANK YOU. Program will now end")
        break

    else:
        print("invalid!, input is not in options")
        continue