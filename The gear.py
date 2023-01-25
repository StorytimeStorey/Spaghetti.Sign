# The Gear
# Last edited by Maverick on 1-19-23
# The Gear takes the Timekeeping, Driver system, and Sign system and combines them.

# Ideas: Put GUI into class.

# To do list:
#
# Small issues:
# Make sure driver times and info combine with timekeeping system.
# Have system that reports driver-to-sign info. 
# 
# Large issues:
# Have fully created GUI interface with The Gear.
# Make sure program is running efficiently.
# Run multiple simulations to weed out edge cases.
# Make sure outputs can be fed into graph systems simply.


import sign_class as SC
from Driver_Class import Driver
import Timekeeping as TimeK 
# sign_class imported as SC so I don't have to type the whole thing.
# Timekeeping imported as TimeK instead of TK to avoid collision with the TK/TTK GUI.


# Placeholder values for the input fields from the GUI.
# simulated_weeks is a multiplier for the simulated_seconds, 2 = 2 weeks while something like 1.42 = 1 week, 3 days.
simulated_weeks = 2
simulated_drivers_number = 20
simulated_slide_numbers = 15
simulated_slide_speed = 10
simulated_slide_order = "slideshow"
drivers = 0
tracker = 0

# Placeholder system for testing if time was working.
total_time = TimeK.seconds_in_week*simulated_weeks
while TimeK.current_second <= total_time:
    TimeK.current_second = TimeK.current_second + 1
    # print(TimeK.current_hour(TimeK.current_second))


# The function that makes all da rules. This will take all input fields from the GUI and send that data to the
# Driver Class, the Sign Class, and the Timekeeping system.
def run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed, simulated_slide_order):

    # System to create drivers.
    drivers = [Driver(f'Driver {i}', Attendance_average=2.6, speedmin=10, speedmax=20, varmin=1, varmax=5) for i in range(simulated_drivers_number)]
    
    # System to setup sign and the cycle_sign method.
    sign_setup = SC.cycle_sign(simulated_slide_speed, simulated_weeks, True)
    tracker = 0
    for i in range(simulated_slide_numbers):
        tracker += 1
        thing = SC.sign_node(str(tracker))
        sign_setup.append(thing)
    sign_setup.cycle_image()

    # Setup for the Timekeeping module.
    TimeK.seconds_in_week = 604800 * simulated_weeks
    TimeK.current_second = 0
    # local variables for keeping track of the day or hour.
    the_day = ""
    the_hour = 0
    # while loop that updates TimeK's total time.
    while TimeK.current_second <= total_time:
        TimeK.current_second = TimeK.current_second + 1

        # Checks if the_day variable is different from TimeK's current day.
        # If so, update the_day variable.
        # Will be used for creating queue of drivers for the day.
        if TimeK.current_day(TimeK.current_second) != the_day:
            the_day = TimeK.current_day(TimeK.current_second)
            print(the_day)
        
        # Checks if the_hour variable is different from TimeK's current hour.
        # If so, update the_hour variable.
        # Will be used for creating queue of drivers for the hour, and then simulating the drive up.
        if TimeK.current_hour(TimeK.current_second) != the_hour:
            the_hour = TimeK.current_hour(TimeK.current_second)
            print(the_hour)

            
    # Checks if the_hour is the same number as TimeK's current_hour. If not, start running the list of the drivers for that
    # hour to get their data and update the hour.
    # if TimeK.current_hour != the_hour:
    #     the_hour = TimeK.current_hour
    #     print(the_hour)



    # Simulation needs:
    # Have signs cycling in proportion to Timekeeping.
    # Have drivers queued up after each hour.
    # Have driver_speed generate /seperately/ from each driver, then used on driver.
    # Create holder for signs each student has observed.
    #       -Should the holder be a list or a dictionary?
    # Re:Small issues: Have system that reports driver-to-sign info.

    # Set up driver queue on a per day basis.
        # Check and start portion of the queue 

run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed, simulated_slide_order)