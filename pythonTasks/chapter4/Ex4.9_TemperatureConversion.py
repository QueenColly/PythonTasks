#Exercise4.9 Temperature Conversion

def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>10} {'Fahrenheit':>10}")
for c in range(101):
    print(f"{c:10.1f} {fahrenheit(c):10.1f}")
