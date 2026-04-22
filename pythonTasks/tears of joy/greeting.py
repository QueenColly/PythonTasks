#. Repeat a greeting
#Ask the user for their name once, then print 'Hello, <name>!' five times using loop.
#Expected output (name = Adeola): Hello, Adeola! is printed 5 times
#



user_name = (input('What is your name?'))
print('Hello ' , user_name ,'!!..')
for number in range(5):
    print('Hello',user_name ,'!!!..')
