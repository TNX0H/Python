from sys import argv
script_name,output, rate, prize = argv
a = (int(output) * int(rate)) + int(prize)

print(a)