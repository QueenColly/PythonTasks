
#Exercise4.13 Arbitrary Argument List

def product(args):
    result = 1
    for num in args:
        result *= num
    return result

print(product(1, 2, 3))    # 6
print(product(5, 10, 2))   # 100
