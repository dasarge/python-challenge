import os
import csv


def average_list(names):
    count = len(names)
    total = 0.00
    for x in names:
        total += x
    return total/count


with open('Book1.csv', 'r') as file:
    reader = csv.reader(file)
    book = []
    for row in reader:
        book.append(int(row[1]))
    print(book)
    avg = average_list(book)
    print(avg)
