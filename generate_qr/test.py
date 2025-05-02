def fizzBuzz(n):
    for i in range(n):
        if (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
            print(i + 1)
        elif (i + 1) % 3 == 0 and (i + 1) % 5 != 0:
            print("Fizz")
        elif (i + 1) % 3 != 0 and (i + 1) % 5 == 0:
            print("Buzz")
        elif (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            print("FizzBuzz")
            break

        i += 1


if __name__ == "__main__":
    fizzBuzz(15)
