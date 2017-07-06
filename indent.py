#!/usr/local/bin/python3

file = open("data.txt")
lines = file.readlines()

for line in lines:
    print line

print lines[1]
file.close()