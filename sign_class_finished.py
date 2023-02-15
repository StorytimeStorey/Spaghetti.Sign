import Timekeeping as TimeK
import random
import json

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
        self.signs_seen_count = {}
        self.driver_memory = {}

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
        If the sign has been seen, it'll increment the count
        If it hasn't been seen, it'll add that sign to the dictionary and set the counter to 1
        """
        # creates dict in format {image: times seen}
        if image in self.signs_seen_count:
            self.signs_seen_count[image] += 1
        else:
            self.signs_seen_count[image] = 1
        # creates dict in format {driver: list of signs seen}
        if driver in self.driver_memory:
            self.driver_memory[driver].append(image)
        else:
            self.driver_memory[driver] = [image]

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
                # move to the next image every [viewing_time] increments
                if second%self.viewing_time == 0:
                    with open('booleans.json') as file:
                        booleans = json.load(file)
                    if  booleans["cycle_type"] == True:
                        # cycles the slides in the order they were created
                        #print('cycle')
                        #print(booleans["cycle_type"])
                        self.current_image = self.current_image.next
                        cycle_time = 0
                    else: 
                        # randomly cycles the slides
                        #print('random')
                        #print(booleans['cycle_type'])
                        for i in range(random.randint(1, TimeK.simulated_slide_numbers)):
                            self.current_image = self.current_image.next

                else:
                    cycle_time += 1
            TimeK.time_elapsed += 604800







if __name__ == "__main__":
    #Put testing in here
    
    pass
# testing_sign = sign(5, 1, True)
# tracker = 0 
# for thing in range(20):
#     tracker += 1
#     bro = sign_node(tracker)
#     testing_sign.append(bro)
# testing_sign.cycle_image()
    # print(testing_sign.current_image)


# testing_sign.cycle_image()
# print(testing_sign)


