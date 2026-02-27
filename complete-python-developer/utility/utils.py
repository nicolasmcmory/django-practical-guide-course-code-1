import sys
from random import randint
from os import walk


def fun_fun():
    num = randint(1, 10)
    choice = (input("guess number 1 to 10: "))
    while int(choice) != num:
        choice= int(input("Try again:"))

def file_getter_reader(file_path):
    with open(file_path, mode='a') as file:
        file.write("extra")