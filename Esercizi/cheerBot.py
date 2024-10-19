import time

def cheer(s):
    for c in s:
        if (c != ' '):
            print(f'give me {c}!!')
            time.sleep(1)

    for e in range(0,10):
        print(s + '!'*20)    


if __name__ == '__main__':
    s = input('let me cheer on: ')
    cheer(s)
    