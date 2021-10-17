import random

def gen_random(count, begin, end):
    for i in range(count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    print(list(gen_random(3, 1, 100)))
    print(list(gen_random(10, 0, 20)))
    print(list(gen_random(20, 0, 3)))
