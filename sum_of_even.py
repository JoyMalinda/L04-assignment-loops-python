def sum_of_even():
    num = int(input("Enter a number: "))
    
    sum1 = 0
    for i in range(num + 1):
        if i <= num and i % 2 == 0:
            sum1 += i
        elif i == num and i % 2 != 0:
            break
    print(f"The sum of even numbers up to {num} is {sum1}")

sum_of_even()