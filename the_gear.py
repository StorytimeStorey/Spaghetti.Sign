# The Gear
# Edited by 2-9-23
# The Gear takes the Timekeeping, Driver_Class, sign_class, and the GUI modules and executes everything.

import sign_class_finished as SC
import Driver_Class as DriverC
import Timekeeping as TimeK
import GUI as GUI

simulated_weeks = 6
simulated_drivers_number = 20
simulated_driver_days = 3
simulated_slide_numbers = 15
simulated_slide_speed = 10
simulated_slide_order = "slideshow"
drivers = 0
tracker = 0

def run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed):

    # System to create drivers.
    DriverC.amount_of_students = simulated_drivers_number
    studentsSim = DriverC.Student_Queue()

    # creates the sign, populating it with images
    the_sign = SC.sign(simulated_slide_speed, simulated_weeks, True)
    tracker = 0
    for i in range(simulated_slide_numbers):
        tracker += 1
        image = SC.sign_node(str(tracker))
        the_sign.append(image)
    # this does the whole simulation essentially. Look at the sign class for more details
    the_sign.cycle_image(studentsSim.drivers)
    return the_sign.signs_seen_count

DriverC.amount_of_students = simulated_drivers_number

print(run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed))
def testing_function():
    pass
# GUI.run_gui(slide_arrange_button_R_func=testing_function, 
#             slide_arrange_button_S_func=testing_function, 
#             run_sim= lambda: run_simulation(simulated_weeks, 
#                                             simulated_drivers_number, 
#                                             simulated_slide_numbers, 
#                                             simulated_slide_speed, 
#                                             simulated_slide_order))