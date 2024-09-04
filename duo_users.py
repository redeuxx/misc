import csv
import os

users = []

def main():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[1])
            if row[1] not in users:
                users.append(row[1])

    for user in users:
        with open('users.txt', 'a') as file:
            file.write(user + '\n')
    print(len(users))

if __name__ == '__main__':
    main()