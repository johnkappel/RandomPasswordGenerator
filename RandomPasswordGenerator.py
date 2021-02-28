
import random

passlen = int(input("Please enter the number of characters for your new passwaord:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&*?"
p = "".join(random.sample(s,passlen ))

print (p)
