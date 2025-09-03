"""
Authors: Owen Cook, Wayne Yu
Creation Date: 2025/09/03
Program: Calculates speeding ticket fine based on speed limit and actual speed
"""


def speeding_ticket():
    # User input for limit and speed
    limit = input()
    speed = input()

    # Calculate difference in limit and speed
    diff = int(speed) - int(limit)

    # Driving 10 mph under the speed limit (or slower) receives a $50 ticket
    if diff <= -10:
        ticket = 50
    # Driving 6 - 20 mph over the speed limit receives a $75 ticket
    elif diff <= 20 and diff >= 6:
        ticket = 75
    # Driving 21 - 40 mph over the speed limit receives a $150 ticket
    elif diff > 20 and diff <= 40:
        ticket = 150
    # Driving faster than 40 mph over the speed limit receives a $300 ticket
    elif diff > 40:
        ticket = 300
    # No ticket otherwise
    else:
        ticket = 0

    print(ticket)

if __name__ == '__main__':
    speeding_ticket()
