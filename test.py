import time
import random

def main():
    t = random.randint(10, 20)
    print(t)
    for i in range(t+1):
        print(t-i, end='')
        print('\r', end=' ')
        time.sleep(1)

if __name__ == "__main__":
    main()