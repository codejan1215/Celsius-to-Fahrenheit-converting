'''
converting celsius to fahrenheit
'''

def celsius_to_fahrenheit(celsius) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")

if __name__ == "__main__":
    main()


