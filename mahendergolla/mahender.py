print("EVEN OR ODD GAME")

attempts = 3

while attempts > 0:

    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even Number")

    else:
        print("Odd Number")

    attempts = attempts - 1

    print("Attempts Left:", attempts)

print("GAME OVER")