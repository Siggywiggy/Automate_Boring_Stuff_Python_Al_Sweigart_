import time
import sys
print(f'curent time is {time.time()} seconds since the unix epoch')
print(f'current time is {time.ctime()}')


sys.set_int_max_str_digits(9999999)
def calc_product():
    # calc the product of the first 100 000 numbers
    product = 1
    for i in range(1, 100000):
        product = product * i

    return product

start_time = time.time()

product = calc_product()
end_time = time.time()

print(f'the result is {len(str(product))} digits long')
print(f'the result took {end_time-start_time} seconds to calculate')