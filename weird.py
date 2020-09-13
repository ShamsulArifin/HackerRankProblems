n = input(": ")
d = n % 2
if d == 1:
    print ("weird")
else:
    if n in range(2, 5):
        print ("not weird")
    elif n in range(6, 21):
        print ("weird")
    elif n in range(21, 101):
        print ("not weird")
