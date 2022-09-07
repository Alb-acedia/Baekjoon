from sys import stdin, stdout

n = stdin.readline()
a = set(stdin.readline().split())
m = stdin.readline()
b = stdin.readline().split()

for l in b:
    stdout.write("1\n") if l in a else stdout.write("0\n")
