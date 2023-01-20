# The Gear
# Last edited by Maverick on 1-19-23
# The Gear takes the Timekeeping, Driver system, and Sign system and combines them.

# To do list:
#
# Small issues:
# Get time system properly moving.
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
# from Driver_Class import Driver
import Timekeeping as TimeK 


simulated_weeks = 2
total_time = TimeK.seconds_in_week*simulated_weeks
while TimeK.current_second <= total_time:
    TimeK.current_second = TimeK.current_second + 1
    # print(TimeK.curren)




