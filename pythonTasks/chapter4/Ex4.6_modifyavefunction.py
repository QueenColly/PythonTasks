#Exercise 4.6 Modified average Function

def average(first_num, *args):
    total = first_num + sum(args)
    count = 1 + len(args)
    return total / count

# Testing
print(average(10, 20, 30))

# average()  <-- This will cause a TypeError as required
