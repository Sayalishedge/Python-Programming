##import mymodul1
##
##mymodul1.f1()
##mymodul1.f2(23)
##mymodul1.f3()

##import mymodul1 as m1
##m1.f1()
##m1.f2(34)
##m1.f3()

import sys
sys.path.append(r"c:\mydata")
from mymodul1 import *
f1()
f2(34)
f3()
