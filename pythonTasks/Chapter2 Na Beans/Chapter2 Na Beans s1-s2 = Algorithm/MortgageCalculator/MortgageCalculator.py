principal = int (input("Enter the principal amount:"))
annual rate = float(input("Enter the annual rate in %:"))
duration = int (input("Enter the duration in year: "))
principal = annualrate*(1+ annualrate)** duration/(1 + annualrate)* duration -1
mortgage = principal
print ("mortgage is : " , mortgage)
