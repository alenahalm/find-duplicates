import os
import math
import random
import time


def Time(string_to_hash, func: callable):
    t = time.perf_counter()
    func(string_to_hash)
    print(f"Elapsed {time.perf_counter() - t}")


def CRC(string):
    h = 0
    for i in string:
        highorder = h & 0xf8000000
        h = h << 5
        h = h ^ (highorder >> 27)
        h = h ^ ord(i)
    return h


def PJW(string):
    h = 0
    for i in string:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g != 0:
            h = h ^ (g >> 24)
            h = h ^ g
    return h


def R(char):
    lst = []
    while len(lst) != 26:
        r = random.randint(1, 26)
        while r in lst:
            r = random.randint(1, 26)
        lst.append(r)
    return lst[ord(char) - 97]


def BUZ(string):
    h = 0
    for i in string:
        highorder = h & 0x80000000
        h = h << 1
        h = h ^ (highorder >> 31)
        h = h ^ R(i)
    return h


def find_duplicates(strings, hash_function: callable):
    lst = []
    duplicates = []
    for i in range(len(strings)):
        if strings[i] not in lst:
            lst.append(hash_function(strings[i]))
        else:
            duplicates.append(i)
    return duplicates


file_names = os.listdir('out/')
files = []
for i in file_names:
    with open('out/' + i, 'r') as f:
        files.append(f.read())
for i in range(len(files)):
    for char in ' ?.!/;:\n\t':
        files[i] = files[i].replace(char, '')
    files[i] = files[i].lower()
# print(files[0])

hash_CRC = find_duplicates(files, CRC)
# hash_PJW = find_duplicates(files, PJW)
# hash_BUZ = find_duplicates(files, BUZ)

counter = 0
for i in hash_CRC:
    if hash_CRC.count(i) > 1:
        counter += 1
# print(counter)

# print(len(hash_CRC))

print(Time(files[0], CRC))
print(Time(files[0], PJW))
print(Time(files[0], BUZ))