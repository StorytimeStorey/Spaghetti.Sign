
import sign_class_finished as SC
import Driver_Class as DriverC
import GUI as GUI
import Timekeeping as TimeK

seconds_in_week = 604800
current_second = 0
time_elapsed = 0
day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
import json
# booleans = open('booleans.json', 'r')

def slide_arrange_button_R_function():
    #print('in r')
    with open('booleans.json') as file:
        booleans = json.load(file)
    booleans['cycle_type'] = False
    with open('booleans.json', 'w') as file:
        json.dump(booleans, file)
    file.close()

def slide_arrange_button_S_function():
    #print('in s')
    with open('booleans.json') as file:
        booleans = json.load(file)
    booleans['cycle_type'] = True
    with open('booleans.json', 'w') as file:
        json.dump(booleans, file)
    file.close()

def current_day(current_second):
    current_day = current_second % seconds_in_week // (24 * 60 * 60)
    return day_list[current_day]

def current_hour(current_second):
    current_hour = current_second % (24 * 60 * 60) // (60 * 60)
    return current_hour

def run_simulation(simulated_weeks, simulated_drivers_number, simulated_slide_numbers, simulated_slide_speed):
    '''
    Inputs:
        simulated_weeks - 
        simulated_drivers_number - 
        simulated_slide_numbers - 
        simulated_slide_speed - 
    Returns:
        {image: times seen}, {driver: signs seen}
    '''
    # print('in run_simulation')
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
    the_sign.cycle_image(studentsSim)
    # print(f'the sign.first_graph is {the_sign.first_graph}')
    TimeK.first_data_to_graph.append(the_sign.first_graph)
    return the_sign.first_graph

first_data_to_graph = []
simulated_weeks = 1
simulated_drivers_number = 20
simulated_driver_days = 3
simulated_slide_numbers = 15
simulated_slide_speed = 10
simulated_slide_order = "slideshow"
drivers = 0
tracker = 0