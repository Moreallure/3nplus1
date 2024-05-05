num = input("Which number do you want to experiment with? ")

n = int(num)

odd = 0
even = 0
highest = n

while True:

    if n % 2 == 0:
        n = n / 2
        odd += 1
    else:
        n = n * 3 + 1
        even += 1

    if (n > highest):
        highest = n

    print(int(n))

    if n == 1:
        break

print("Number Tried: " + num)
print("Total Steps: " + str(odd + even))
print("Odd : Even = " + str(odd) + " : " + str(even))
print("Highest Reached: " + str(int(highest)))