#a pattern that displays pattern 54321 , 4321 , 321, 21 ,1
#display in descending order of 5 numbers
#let your
#
number = int(input("Enter a number: "))
for number in range (number, 0, -1):
    for count in range(number, 0, -1):
      print(count, end=" ")  
    print()
