num = int(input("Which number do you want to start with? "))

n = num

steps = 0

while True:

    if n % 2 == 0:
        n = n / 2
        steps += 1
    else:
        n = (n * 3 + 1) / 2
        steps += 2

    if n == 1:
        print("Number: " + str(num) + " | Steps: " + str(steps))
        num += 1
        n = num
        steps = 0
