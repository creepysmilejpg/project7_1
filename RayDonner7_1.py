def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)


def cat_ears(n):
    if n == 1:
        return 2
    else:
        return cat_ears(n - 1) + 2


def alien_ears(n):
    if n == 1:
        return 2
    elif n % 2 == 1:
        return alien_ears(n - 1) + 2
    elif n % 2 == 0:
        return alien_ears(n - 1) + 3


def main():
    number = int(input('Please enter a number: '))
    powernum = int(input('Please enter the power: '))
    total = power(number, powernum)
    print(f'Your number is: {total}')

    cats = int(input('Please enter the number of cats: '))
    catsears = cat_ears(cats)
    print(f'Number of cat ears: {catsears}')

    aliens = int(input('Please enter the number of aliens: '))
    aliensears = alien_ears(aliens)
    print(f'Number of alien ears: {aliensears}')


if __name__ == '__main__':
    main()
