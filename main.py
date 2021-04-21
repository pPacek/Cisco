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
    text = []
    confdict = {}
    logdict = {}
    with open('./Files/cms_logs.txt', 'r') as f:
        for line in f:
            if 'conference' in line and 'named' in line:
                cid = str(re.findall(r'[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+\-+[a-z0-9]+', line))
                name = re.findall(r'named "(.*)"', line)
                for i in name:
                    confdict[cid] = i

    with open('./Files/cms_logs.txt', 'r') as f:
        for line in f:
            if 'Apr 5' or 'Apr 6' or 'Apr 7' in line:
                if 'joined conference' in line:
                    a = re.findall(r'\w+\s+\d+\s+\d+:\d+:\d+\.\d+', line)
                    b = re.findall(r'"(.*)"', line)
                    c = str(re.findall(r'conference (.*) via', line))
                    for j in a:
                        logdict['time'] = j
                    for k in b:
                        logdict['name'] = k
                    logdict['conference'] = confdict[c]
                    for x, y in logdict.items():
                        z = f"{x} : {y} "
                        text.append(z)
                    text.append('\n')

    with open('./Files/logged.txt', 'w') as f:
        for element in text:
            f.write(str(element) + '\n')

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
