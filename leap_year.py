#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program is check leap year


def main():
    # this function is check leap year

    # input
    year = int(input("Enter the year: "))
    print("")

    # process & output
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("It is not a leap year")
        else:
            print("It is a leap year")
    else:
        print("It is not a leap year")


if __name__ == "__main__":
    main()
