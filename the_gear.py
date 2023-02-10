# The Gear
# Edited by 2-9-23
# The Gear takes the Timekeeping, Driver_Class, sign_class, and the GUI modules and executes everything.

import sign_class_finished as SC
import Driver_Class as DriverC
import Timekeeping as TimeK
import GUI as GUI

simulated_weeks = 2
simulated_drivers_number = 20
simulated_driver_days = 3
simulated_slide_numbers = 15
simulated_slide_speed = 10
simulated_slide_order = "slideshow"
drivers = 0
tracker = 0

# start_drive will be the method that actually simulates driving up the road to the sign.
# A local version of the sign_class will be ran in order to make sure it can properly function without
# messing up or slowing down the simulation's main sign.

# The fog is coming.
def start_drive(current_driver, drive_speed, tracker):
    artif_sign_tracker = tracker

    # We weren't able to properly integrate the sign_class's system into start_drive, so
    # instead an artificial sign and cycling system is created to do the calcuations and doesn't
    # affect the actual sign_class.
    artif_sign_speed = simulated_slide_speed
    artif_sign_start_point = SC.cycle_time
    artif_sign_number = simulated_slide_numbers
    artif_sign_clock = artif_sign_start_point

    drive_time = 0
    
    # Recording lasts until the drive_time has reached the drive_speed generated during run_simulation.
    while drive_time > drive_speed:
        drive_time = drive_time + 1
        artif_sign_clock = artif_sign_clock + 1

        # checks if the clock has reached the speed of the sign. If so, cycle to the next sign.
        if artif_sign_clock == artif_sign_speed:
            artif_sign_tracker = artif_sign_tracker + 1
        # checks if the sign has reached the end of signs. If so, cycle back to the first sign.
        if artif_sign_tracker == artif_sign_number:
            artif_sign_tracker = 0
        # Sends whichever sign it got from the while loop off to the current_driver's "signs_seen" function to
        # be added to their "data"
        DriverC.Driver.signs_seen(artif_sign_tracker)


# Believe it or not, it runs the simulation.
def run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed, simulated_slide_order):

    # System to create drivers.
    DriverC.amount_of_students = simulated_drivers_number
    studentsSim = DriverC.Student_Queue()

    # System to setup sign and the cycle_sign method.
    # Note: the sign cycling runs /independent/ of TimeKeeping. But since they're executed at the same time,
    # they should be working in tandem.
    sign_setup = SC.cycle_sign(simulated_slide_speed, simulated_weeks, True)
    tracker = 0
    for i in range(simulated_slide_numbers):
        tracker += 1
        thing = SC.sign_node(str(tracker))
        sign_setup.append(thing)
    # sign_setup.cycle_image()
    # Setup for the Timekeeping module.
    TimeK.seconds_in_week = 604800 * simulated_weeks
    TimeK.current_second = 0
    # local variables for keeping track of the day or hour.
    the_day = ""
    the_hour = 0
    total_time = TimeK.seconds_in_week


    # This does all the magic. This will be the main simulation loop, counting the seconds until we reach the end.
    # Every second, it will check to see if any of the drivers arrive at the current time 
    while TimeK.current_second <= total_time:
        TimeK.current_second = TimeK.current_second + 1
        sign_setup.cycle_image()

        # Every cycle, the linked list will go through its nodes and check if any driver's arrival_time matches the current_second.
        # If so, generate a drive speed and (yet to be implemented) simulate them driving up the hill and recording the signs they saw.
        current_driver = studentsSim.head
        while current_driver != None:
            current_driver = current_driver.next
            if TimeK.current_second in current_driver.DriverC.Driver.arrival_time:
                drive_speed = DriverC.Driver.generate_drive_speed()
                # Note to self: Have start_drive also grab the cycle timer from the sign_class and then use it to create an artificial
                # sign_class to record data from.
                start_drive(current_driver, drive_speed, tracker)
                print("DING!")
                
                



        # Checks if the_day variable is different from TimeK's current_day.
        # If so, update the_day variable.
        # Will be used for creating queue of drivers for the day.
        if TimeK.current_day(TimeK.current_second) != the_day:
            the_day = TimeK.current_day(TimeK.current_second)
            print(the_day)
        
        # Checks if the_hour variable is different from TimeK's current_hour.
        # If so, update the_hour variable.
        # Will be used for creating queue of drivers for the hour, and then simulating the drive up.
        if TimeK.current_hour(TimeK.current_second) != the_hour:
            the_hour = TimeK.current_hour(TimeK.current_second)
            # print(the_hour)

    # Simulation needs:
    # Have driver_speed generate /seperately/ from each driver, then used on driver.
    # Re:Small issues: Have system that reports driver-to-sign info.

    # Data Capture system:
    # Driver generates schedule.
    # System checks if current time has any drivers queued during it.
    # Current sign information is reported to driver.
        # Driver is actively checking if it's seen the sign before. If not, add it to the dictionary.

    # Set up driver queue on a per day basis.
        # Check and start portion of the queue 

        #test command for running simulation.
# run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed, simulated_slide_order)

# DriverC.amount_of_students = simulated_drivers_number
# print(DriverC.amount_of_students)


GUI.run_gui()