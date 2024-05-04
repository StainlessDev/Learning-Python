def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def convert_temperature():
    while True:
        try:
            temperature_input = input("Enter the temperature (or 'quit' to exit): ")
            if temperature_input.lower() == "quit":
                break
            
            temperature_value = float(temperature_input)

            unit_input = input("Enter the unit of measurement (Celsius or Fahrenheit): ")
            unit = unit_input.lower()

            if unit == "celsius":
                converted_temperature = celsius_to_fahrenheit(temperature_value)
                converted_unit = "Fahrenheit"
            elif unit == "fahrenheit":
                converted_temperature = fahrenheit_to_celsius(temperature_value)
                converted_unit = "Celsius"
            else:
                print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")
                continue
            
            print(f"The temperature is {converted_temperature:.2f} {converted_unit}")
        
        except ValueError:
            print("Invalid input. Please enter a numeric temperature.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    convert_temperature()