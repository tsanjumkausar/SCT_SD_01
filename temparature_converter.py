def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    print("🌡️ Temperature Converter")
    print("Supported units: Celsius (C), Fahrenheit (F), Kelvin (K)")
    
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            from_unit = input("Convert from (C/F/K): ").strip().upper()
            to_unit = input("Convert to (C/F/K): ").strip().upper()

            if from_unit == to_unit:
                print(f"No conversion needed. Temperature is {value}°{to_unit}")
                break

            if from_unit == "C":
                if to_unit == "F":
                    result = celsius_to_fahrenheit(value)
                elif to_unit == "K":
                    result = celsius_to_kelvin(value)
                else:
                    raise ValueError
            elif from_unit == "F":
                if to_unit == "C":
                    result = fahrenheit_to_celsius(value)
                elif to_unit == "K":
                    result = fahrenheit_to_kelvin(value)
                else:
                    raise ValueError
            elif from_unit == "K":
                if to_unit == "C":
                    result = kelvin_to_celsius(value)
                elif to_unit == "F":
                    result = kelvin_to_fahrenheit(value)
                else:
                    raise ValueError
            else:
                raise ValueError

            print(f"\n✅ {value}°{from_unit} = {result:.2f}°{to_unit}")
            break

        except ValueError:
            print("❌ Invalid input. Please try again with valid units and numbers.\n")

if __name__ == "__main__":
    convert_temperature()
