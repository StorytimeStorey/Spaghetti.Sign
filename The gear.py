# The Gear
# Last edited by Maverick on 1-19-23
# The Gear takes the Timekeeping, Driver system, and Sign system and combines them.

# To do list:
#
# Small issues:
# Make readable driver creation/initializing system.
# Make sure driver times and info combine with timekeeping system.
# Have system that reports driver-to-sign info.
# 
# Large issues:
# Have fully created GUI interface with The Gear.
# Make sure program is running efficiently.
# Run multiple simulations to weed out edge cases.
# Make sure outputs can be fed into graph systems simply.


from sign_class import cycle_sign
from Driver_Class import Driver
import Timekeeping as TimeK 


# Placeholder values for the input fields from the GUI.
# simulated_weeks is a multiplier for the simulated_seconds, 2 = 2 weeks while something like 1.42 = 1 week, 3 days.

simulated_weeks = 2
simulated_drivers = 20
simulated_slide_numbers = 15
simulated_slide_speed = 5
simluated_slide_order = "slideshow"
drivers = 0


# Placeholder system for testing if time was working.
total_time = TimeK.seconds_in_week*simulated_weeks
while TimeK.current_second <= total_time:
    TimeK.current_second = TimeK.current_second + 1
    # print(TimeK.current_hour(TimeK.current_second))


# The function that makes all da rules. This will take all input fields from the GUI and send that data to the
# Driver Class, the Sign Class, and the Timekeeping system.
def run_simulation(simulated_weeks, simulated_drivers, simulated_slide_numbers, simulated_slide_speed, simulated_slide_order):
    TimeK.seconds_in_week = 604800 * simulated_weeks
    TimeK.current_second = 0

    for i in simulated_drivers:
        drivers[i] = Driver(f'Driver {i}', Attendance_average=2.6, speedmin=10, speedmax=20, varmin=1, varmax=5)


