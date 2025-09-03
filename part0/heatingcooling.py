"""
Authors: Owen Cook, Wayne Yu
Creation Date: 2025/09/03
Program: Calculates heating and cooling days based on average temperature input
"""
def heatingcooling():
    # Initialize heating and cooling count
    heating = 0
    cooling = 0
    # Loop for user input of temperatures
    while True:
        temp = int(input("Enter the average daily temperature: "))
        # Loop end condition
        if temp < -459:
            break
        # Heating day case
        if temp < 60:
            heating += 1
        # Cooling day case
        elif temp > 80:
            cooling += 1
    return heating, cooling

if __name__ == '__main__':
    heating, cooling = heatingcooling()
    print("Heating days: ", heating)
    print("Cooling days: ", cooling)