import Timekeeping as TimeK
import random
import json
from statistics import mean

#cycle_type = json.load(open('cycle_type.json', 'r'))

class sign_node:
    def __init__(self, image):
        '''
        '''
        self.image = image
        self.next = None

    def __repr__(self):
        '''
        Repr to return image
        '''
        return str(self.image)

class sign:
 
    def __init__(self, viewing_time: int, run_time: int, is_running = False):
        '''
        inputs:
        viewing_time - determines how many simulated seconds an image stays on the sign
        run_time - determines how many weeks to cycle for
        is_running - determines if the sign is cycling or not, True means it is, False it is not. Default to False.
        '''
        # create the head of the list and current image, both default as None.
        self.head = None
        self.current_image = None
        self.viewing_time = viewing_time
        self.run_time = run_time
        self.is_running = is_running
        # dict in format {image: times seen}
        self.signs_seen_count = {}
        # creates dict in format {driver: list of signs seen}
        self.driver_memory = {}
        # dict in format {days_attending: self.driver_memory}
        self.attendance_tracker = {}
        # lists for the number of unique signs each driver has seen
        self.days_5 = []
        self.days_4 = []
        self.days_3 = []
        self.days_2 = []
        self.days_1 = []
        # average unique signs seen for how many days of attendance
        self.days_5_mean = 0
        self.days_4_mean = 0
        self.days_3_mean = 0
        self.days_2_mean = 0
        self.days_1_mean = 0
        # percent signs seen for how many days of attendance
        self.days_5_percent = 0
        self.days_4_percent = 0
        self.days_3_percent = 0
        self.days_2_percent = 0
        self.days_1_percent = 0
        # dict in format: {'Days Attended': [1, 2, 3, 4, 5],'Percentage of Signs Seen': [percent values]}
        self.percent_seen_graph_dict = {}


    def __repr__(self):
        '''
        repr method that returns each item in the linked list with arrows showing links
        '''
        str_to_return = str(self.head)
        current_node = self.head
        # loop through linked list and print each item in order with arrows pointing to their next value
        while current_node.next is not self.head:
            str_to_return += f' --> {current_node.next}'
            current_node = current_node.next
        return str_to_return

    # append function for linked list
    def append(self, image):
        '''
        append method for linked list, adds the input image to the end of the linked list, making the 
        image.next value self.head
        '''
        # if there is not a head, make the input image the head
        if not self.head:
            self.head = sign_node(image)
            self.head.next = self.head
        # if there is already a head, add the input image to the end of the linked list
        else:
            current = self.head
            # cycles to the end of the linked list, makes the input image the .next of the current last node and 
            #makes the input image.next the head
            while current.next != self.head:
                current = current.next
            new_node = sign_node(image)
            new_node.next = self.head
            current.next = new_node

    def seen_signs(self, image, driver):
        """
        This function keeps track of how many times each sign has been seen
        Inputs:
            image - the image that was seen
            driver - the current driver, that saw the image

        """
        # populate unique_signs
        if not image in driver.unique_signs:
            driver.unique_signs.append(image)
        # print(driver.unique_signs)

        # make a graph that is percent of signs seen versus days attended
        # dict must be in format: {'Days Attended': [1, 2, 3, 4, 5],'Percentage of Signs Seen': [percent values]}

    def write_dicts(self):

        # populates all the unique signs lists 
        for driver in self.drivers:
            print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
            driver_days_attending = sum(driver.days_attending)
            if driver_days_attending == 5:
                # print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
                total_unique_signs_seen = len(driver.unique_signs)
                self.days_5.append(total_unique_signs_seen)

            elif driver_days_attending == 4:
                # print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
                total_unique_signs_seen = len(driver.unique_signs)
                self.days_4.append(total_unique_signs_seen)

            elif driver_days_attending == 3:
                # print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
                total_unique_signs_seen = len(driver.unique_signs)
                self.days_3.append(total_unique_signs_seen)

            elif driver_days_attending == 2:
                # print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
                total_unique_signs_seen = len(driver.unique_signs)
                self.days_2.append(total_unique_signs_seen)

            elif driver_days_attending == 1:
                # print(f'driver {driver.ID} unique signs is {driver.unique_signs}')
                total_unique_signs_seen = len(driver.unique_signs)
                self.days_1.append(total_unique_signs_seen)
        # find the average unique signs seen for each days_attending
        if len(self.days_5) > 0:
            self.days_5_mean = mean(self.days_5)
        if len(self.days_4) > 0:
            self.days_4_mean = mean(self.days_4)
        if len(self.days_3) > 0:
            self.days_3_mean = mean(self.days_3)
        if len(self.days_2) > 0:
            self.days_2_mean = mean(self.days_2)
        if len(self.days_1) > 0:
            self.days_1_mean = mean(self.days_1)

        # find the percent unique signs seen for each days_attending
        self.days_5_percent = 100*((self.days_5_mean)/(TimeK.simulated_slide_numbers))
        self.days_4_percent = 100*((self.days_4_mean)/(TimeK.simulated_slide_numbers))
        self.days_3_percent = 100*((self.days_3_mean)/(TimeK.simulated_slide_numbers))
        self.days_2_percent = 100*((self.days_2_mean)/(TimeK.simulated_slide_numbers))
        self.days_1_percent = 100*((self.days_1_mean)/(TimeK.simulated_slide_numbers))
        percent_list = [self.days_5_percent, 
                        self.days_4_percent, 
                        self.days_3_percent, 
                        self.days_2_percent, 
                        self.days_1_percent]
        # write dict in format: {'Days Attended': [1, 2, 3, 4, 5],'Percentage of Signs Seen': [percent values]}
        self.percent_seen_graph_dict["Days Attended"] = [1, 2, 3, 4, 5]
        self.percent_seen_graph_dict["Percentage of Signs Seen"] = percent_list
        print(self.percent_seen_graph_dict)
        with open('JSON/results.json', 'w') as file:
            print('writing')
            file.truncate()
            file.write(str(self.percent_seen_graph_dict))
            file.close()





    def cycle_image(self, drivers):
        '''
        Cycles through the images, leaving each image as current_image for [viewing time] 
        Inputs:
            drivers - list of all drivers
            cycle_type - True/False statement, True means circular cycle, False means random cycle
        '''
        global cycle_time
        cycle_time = 0
        self.current_image = self.head
        self.drivers = drivers
        # tracks number of weeks passed during the current runtime
        self.num_weeks = TimeK.simulated_weeks
        weeks_passed = 0
        driver_leave_time = 0
        # loop through linked list, pausing for the inputted viewing time on each node.
        for week in range(self.num_weeks):
            print(TimeK.simulated_weeks)
            print(self.run_time)
            print(week)
        #driveway dictionary for keeping track of currently queued drivers on the road
        #Key is the Driver ID, Value is their current amounzt of seconds for this drive
            driveway = {}
            drivers_to_remove = [] #Python doesn't allow you to delete keys on iteration, so I had to come up with a workaround
            for second in range (604801):

                #First thing in loop is to check if any drivers on the driveway need to be removed
                for d in drivers_to_remove:
                    del driveway[d]
                #If drivers were removed, clear the list. If not, this does nothing
                drivers_to_remove = []
                TimeK.current_second = second
<<<<<<< Updated upstream
                #At the start declae the first student
                if second == 0:
                    current_driver = drivers.head
                #while look to check if there's anyone in the same second that needs to be queued
                while second in current_driver.driver.arrival_time:
                    #Put the driver in the driveway, key is generated speed + seconds
                    driveway[current_driver.driver.ID] = current_driver.driver.generate_drive_speed()+second
                    #Checking for last driver, resets it to the head
                    if current_driver.next != None:
                        current_driver = current_driver.next
                    else:
                        current_driver = drivers.head
                #This controls when the driver needs to be removed from the driveway
                for driver in driveway:
                    if second < driveway[driver]:
                        self.seen_signs(image=self.current_image.image, driver=current_driver.driver)
                    else:
                        #driver_leave_time = 0
                        #append the driver to be removed, will happen at the beginning of the next iteration
                        drivers_to_remove.append(driver)
=======
                # generate driver speed and calculate the time at which the driver can no longer see the sign, for every driver
                for driver in self.drivers:
                    # checks if the  current second matches any of the driver arrival times, if it does generates a drive speed
                    if second in driver.arrival_time:
                        driver_speed = driver.generate_drive_speed()
                        # calculate the time the driver leaves
                        driver_leave_time = second+driver_speed
                    # add the current image to the drivers data if they can see it
                    if second < driver_leave_time:
                        self.seen_signs(image=self.current_image.image, driver=driver)
                    if second == driver_leave_time:
                        driver_leave_time = 0
>>>>>>> Stashed changes
                # move to the next image every [viewing_time] increments
                if second%self.viewing_time == 0:
                    with open('JSON/booleans.json') as file:
                        booleans = json.load(file)
                    if  booleans["cycle_type"] == True:
                        # cycles the slides in the order they were created
<<<<<<< Updated upstream
                        #print('cycle')
                        #print(booleans["cycle_type"])
=======
>>>>>>> Stashed changes
                        self.current_image = self.current_image.next
                        cycle_time = 0
                    else: 
                        # randomly cycles the slides
<<<<<<< Updated upstream
                        #print('random')
                        #print(booleans['cycle_type'])
=======
>>>>>>> Stashed changes
                        for i in range(random.randint(1, TimeK.simulated_slide_numbers)):
                            self.current_image = self.current_image.next

                else:
                    cycle_time += 1
            TimeK.time_elapsed += 604800
<<<<<<< Updated upstream







if __name__ == "__main__":
    #Put testing in here
    
    pass
# testing_sign = sign(5, 1, True)
# tracker = 0 
# for thing in range(20):
#     tracker += 1
#     bro = sign_node(tracker)
#     testing_sign.append(bro)
=======
            self.num_weeks += 1
            # stop cycling once desired run_time is reached
            # self.write_dicts()
            if self.num_weeks == self.run_time:
                results = self.write_dicts()
                self.is_running = False
        return results


testing_sign = sign(5, 1, True)
tracker = 0 
for thing in range(20):
    tracker += 1
    bro = sign_node(tracker)
    testing_sign.append(bro)
>>>>>>> Stashed changes
# testing_sign.cycle_image()
    # print(testing_sign.current_image)


# testing_sign.cycle_image()
# print(testing_sign)


