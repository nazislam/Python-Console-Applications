#!/usr/bin/env python3

# Naz-Al Islam
# 04/30/16
# Printing grades points by names in a table

grades = [
    ("Tyler", [100, 95, 90, 92, 100, 100]),
    ("Timmy", [100, 50, 55, 0, 35, 85]),
    ("Tammy", [100, 100, 100, 95, 98, 92]),
    ("Tanya", [100, 100, 100, 100, 92, 90]),
    ("Tony", [90, 90, 90, 92, 85, 100])]


def getLetter(num):
    """ This function takes the number grade as a variable and will return
    the letter (as a string) that this number grade equates to 
    """
    if num < 65:
        return 'F'
    elif num < 75:
        return 'D'
    elif num < 85:
        return 'C'
    elif num < 95:
        return 'B'
    else:
        return 'A'


def main():
    """ This main function will print each student's name and average grade,
    and will also call the getLetter function to also print the letter
    grade that equates to the number grade of the average... 
    """
    s = 0
    for i in numbers:
        s = s + i
    r = round(s / len(numbers), 2)
    return r                        


for (name, numbers) in grades:
    print(name, '\t', main(), '\t', getLetter(main()))
    
if __name__ == "__main__":
    main() 
