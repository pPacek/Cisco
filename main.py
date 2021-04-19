import random
import re


def rectangle():
    a = int(input("write a: "))
    b = int(input("write b: "))
    for i in range(a):
        for j in range(b):
            print('*', end="")
        else:
            print('')


def game():
    n = random.randint(0, 100)
    i = 0
    while n < 100:
        i += 1
        user = int(input("Write a number: "))
        if user == n:
            print(f'wow you got this in {i} attempt')
            break
        elif user < n:
            print("The secret number is higher")
        else:
            print("The secret number is lower")


def search():
    text= []
    with open('./Files/cms_logs.txt', 'r') as f:
        for line in f:
            if 'Apr 5' or 'Apr 6' or 'Apr 7' in line:
                if 'joined conference' in line:
                    a = re.findall(r'\w+\s+\d+\s+\d+:\d+:\d+\.\d+', line)
                    b = re.findall(r'\"+\w+\s+\w+\"+', line)
                    c = re.findall(r'\w+\s+[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+', line)
                    text.append(a+b+c)

    with open('./Files/logged.txt', 'w') as fr:
        for element in text:
            fr.write(str(element)+'\n')


def main():
    x = int(input())
    if x == 1:
        rectangle()
    elif x == 2:
        game()
    elif x == 3:
        search()
    else:
        print("poop")


if __name__ == '__main__':
    main()
    exit(0)
