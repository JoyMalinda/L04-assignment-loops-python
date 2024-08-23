def natural_numbers():
    num = int(input("Enter a number: "))

    for i in range(1, num + 1):
        if num > 0:
            print(i)
        else:
            print("Error: Please enter a positive number!")

natural_numbers()