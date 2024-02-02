import sys
import time

SEED = 0
FLAG = "not set"

j = 0

# Reading arguments from command line using indicators
stopat = len(sys.argv)-1
if (len(sys.argv) > 1):
    while (stopat > j):
        j += 1
        if sys.argv[j] == '-seed':
            j += 1
            SEED = int(sys.argv[j])
        if sys.argv[j] == '-flag':
            j += 1
            FLAG = sys.argv[j]            
            
time.sleep(20)

print("Exit from seed ", SEED, " with flag", FLAG)
