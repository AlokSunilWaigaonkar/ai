# Chatbot in Python

def remind_name():
    print("Hello, remind me your name.")
    name = input("Enter your Name: ")
    print("What a great name you have, {}!\n".format(name))


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input("Remainder after dividing by 3: "))
    rem5 = int(input("Remainder after dividing by 5: "))
    rem7 = int(input("Remainder after dividing by 7: "))

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {}, that's a good time to start programming!\n".format(age))


def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input("Enter a number: "))
    counter = 0
    while counter <= num:
        print("{}!\n".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input("Enter your option: "))
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print("Correct Answer!")
    print()


def end():
    print("Congratulations, have a nice day!")
    print()


# greet('Bot', '2021')
remind_name()
guess_age()
count()
test()
end()
