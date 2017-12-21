#!/usr/bin/env python3

# Naz-Al Islam
# 04/30/16
# How many years it will take to generate certain amount of money.


def main():
    initial = eval(input('How much money to start? '))
    try:
        apr = eval(input('What is apr? '))
    except SyntaxError:
        apr = eval(input('Please write in decimal: '))
    final = eval(input('What is the amount you want to get to? '))

    def savings(g):
        n = round(initial * (1 + apr), 2)
        return n

    year = 1

    while (initial < final):
        initial = savings(initial)
        print('After year', year, 'the account is at', initial)
        year += 1

if __name__ == '__main__':
    main()
