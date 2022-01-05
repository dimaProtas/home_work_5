# import sys, requests

def gen_nums(nam_max):
    for num in range(1, nam_max + 1, 2):
        yield num

# exit(gen_nums())
# if __name__ in '__main__':
generator = gen_nums(15)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# for i in generator:
#     print(i)





