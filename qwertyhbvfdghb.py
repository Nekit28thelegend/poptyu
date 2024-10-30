def is_prime(func):
    def wrapper(x, y, z):
        res = func(x, y, z)
        r = 0
        for i in (2, 3, 5, 7):
            k = res/i
            p = res % i
            if p == 0 and k > 1:
                print('Составное')
                r = 1
                break
        if r == 0 and res != 0 and res != 1:
            print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(x, y, z):
    s = x+y+z
    return s


result = sum_three(2,3,6)
print(result)