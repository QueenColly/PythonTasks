#
#18. Print a number triangle
#Print a right-angled triangle of numbers with 5 rows.
#Expected output:
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#

for number in range(1,6):
    for count in range(1,number + 1):
        print(count,end=" ")
    print()

