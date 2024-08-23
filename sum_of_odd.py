def sum_of_odd():
    num = int(input("Enter a number: "))
    sum1 = 0
    for i in range(num + 1):
        if i <= num + 1 and i % 2 != 0:
            sum1 += i
        elif i == num and i % 2 == 0:
            break
    print(f"The sum of odd numbers is {sum1}")

sum_of_odd()