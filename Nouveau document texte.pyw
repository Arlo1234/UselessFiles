#This programm creates a giant amount of useless files.
#It takes much more time to delete them than to create them.
#Run at your own risk. I am not responsible to any damage caused by this script

import threading
import time
import sys
import os

if sys.version_info.major == 2:  # pragma: no cover   #if python2
    integer_types = (int, long)
else:  # pragma: no cover
    integer_types = (int,)


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

def dumps(number):
    """Dumps an integer into a base36 string.
    :param number: the 10-based integer.
    :returns: the base36 string.
    modify tho alphabet variable to create more possibilities
    """
    
    if not isinstance(number, integer_types):
        raise TypeError('number must be an integer')

    if number < 0:
        return '-' + dumps(-number)

    value = ''

    while number != 0:
        number, index = divmod(number, len(alphabet))
        value = alphabet[index] + value

    return value or '0'



#Let the fun begin...

def doShit(n):
    x=0
    os.mkdir(str(n))
    while True:
        open (str(n)+"//"+dumps(x), "a").write(str(x))
        x+=1

       

for i in range(100):
    my_dict = {'n':i}
    t = threading.Thread(target=doShit, kwargs=my_dict)
    t.start()

