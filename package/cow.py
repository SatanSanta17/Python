import cowsay
import sys
if len(sys.argv)==2:
    cowsay.cow(f"Hello, {sys.argv[1]}")

