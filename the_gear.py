# The Gear
# Edited by 2-9-23
# The Gear takes the Timekeeping, Driver_Class, sign_class, and the GUI modules and executes everything.

import sign_class_finished as SC
import Driver_Class as DriverC
import Timekeeping as TimeK
import GUI as GUI
from Timekeeping import (simulated_weeks, 
                        simulated_drivers_number, 
                        simulated_driver_days, 
                        simulated_slide_numbers, 
                        simulated_slide_order, 
                        simulated_slide_speed, 
                        drivers, 
                        tracker)

DriverC.amount_of_students = simulated_drivers_number

# print(TimeK.run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed))
def slide_arrange_button_R_function():
    pass
def slide_arrange_button_S_function():
    pass
GUI.run_gui(slide_arrange_button_R_func=slide_arrange_button_R_function, 
            slide_arrange_button_S_func=slide_arrange_button_S_function)