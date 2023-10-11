import sys
from calculator import mul

if len(sys.argv)!=3:
    sys.exit()

mul(int(sys.argv[1]),int(sys.argv[2]))
