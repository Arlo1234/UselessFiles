from secrets import token_hex
from random import randint
while True:
    file1 = open(token_hex ()+"."+token_hex (2),"a")
    file1.write(token_hex (randint(1,1000))+"\n")
    file1.close()
