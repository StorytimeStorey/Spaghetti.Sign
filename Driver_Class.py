# Driver class 
import random

Day_List = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

Attendance_average = 2.6  # This should be a variable in the GUI. 

# Dictate the fastest and slowest speed a student may "drive"
speedmin = 10 
speedmax = 20 

# Variables for how much their speed may vary at any given day
varmin = 1 
varmax = 5

# The number of students that will be called. Should be a in GUI.
amount_of_students = 20

class Node:
    #I'm just a lil node with a node family
    def __init__(self, driver):
        self.driver = driver
        self.next = None

class Student_Queue:
    '''
    Here lies the Queue, hallowed by thy name
    It isn't circular yet. I"m not quite sure how to do that. 
    We cna probably just have it run every time the week starts again if we, as a group, decided
    that none of us knew how a circular queue works.
    '''
    Day_List = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    def __init__(self):
        self.head = None
        self.drivers = [Driver(f'Driver {i}', Attendance_average,speedmin, speedmax, varmin, varmax) for i in range(amount_of_students)]
        self.day_list = Day_List
        self.enqueue_students()

    def enqueue_students(self):
        for second in range(604801):
            for driver in self.drivers:
                if second in driver.arrival_time:
                    current_driver = Node(driver)
                    #call speed randomizer from driver
                    self.add(current_driver)

    def add(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            # node.next = self.head

class Driver:
    """
    Important info to be called are:
        .data is a dictionary for what signs have been seen and how many times
        .arrival_time is a list of times the student will arrive in specific seconds
        def signs_seen(self, message) is the function for increasing the data dictionary
        .schedule is a dictionary of days:hours that the students arrive 
        def generate_drive_speed(self) is the function that gives the student a somewhat random drive speed
            To be called when the driver arrives
        I think that's all the important stuff, honestly. 
    
    """
    def __init__(self, ID, Attendance_average, speedmin, speedmax, varmin, varmax):
        self.ID = ID  # Pretty much just a name, means nothing
        self.attendance_average = Attendance_average 
        self.days_attending = self.days_attended() # What days the student is attending
        self.hour_arrived = self.choose_hour()  # What hours the student will arrive
        self.days_attending_total = sum(self.days_attending)
        self.speed = {} # TO be filled on call
        self.speed["drive_speed"] = random.randint(speedmin, speedmax)
        self.speed["drive_speed_var"] = random.randint(varmin, varmax)
        self.data = {} # Where each students data of what signs it has seen will go
        self.unique_signs = [] # list of unique signs the driver has seen
        self.arrival_time = [] # This is where the SPECIFIC SECONDS in the week the student will arrive will be stored
        self.arrival_time_generator()
        
    def days_attended(self):
        """
        This function returns a list of integers (1 or 0) representing the days that the driver attends.
        The probability of attending each day is based on the average of 2.6 weekdays per week.
        """
        days_attending = []
        for i in range(5):
            if random.uniform(0, 1) < self.attendance_average/5:
                days_attending.append(1)
            else:
                days_attending.append(0)
        return days_attending
    
    def actual_days(self):
        """
        This function uses the zip function to correlate the day_list and the days_attending lists
        and returns a dictionary of the actual names of days the driver will attend with value 1.
        """
        actual_days_dict = {}
        for day, attending in zip(Day_List[1:6], self.days_attending):
            if attending == 1:
                actual_days_dict[day] = 1
        return actual_days_dict


    def class_time_repeating(self):
        """
        This function returns a self.schedule that uses some probability and decides what hours a driver will arrive on what days.
        It uses the mwf/mw/tth general scheduling. It could use some dialing-in. Specifically, I think the function works great
        But how we give each driver their days is what needs work to make this more accurate
        """
        self.schedule = {}
        #These are the weights for the probabilities that decide which hour the student will arrive in
        hourly_prob = {0:0/14,1:0/14,2:0/14,3:0/14,4:0/14,5:1/14,6:1/14,7:7/14,8:3/14,9:7/14,10:3/14,11:7/14,12:3/14,
                        13:1/14,14:1/14,15:1/14,16:1/14,17:1/14,18:1/14,19:1/14,20:1/14,21:0/14,22:0/14,23:0/14}
        daily_prob = hourly_prob

        def mwf_days(self):
            actual_days = self.actual_days().keys()
            if "Monday" in actual_days and "Wednesday" in actual_days and "Friday" in actual_days:
                return True
            else:
                return False

        def mw_days(self):
            actual_days = self.actual_days().keys()
            if "Monday" in actual_days and "Wednesday" in actual_days:
                return True
            else:
                return False

        def tth_days(self):
            actual_days = self.actual_days().keys()
            if "Tuesday" in actual_days and "Thursday" in actual_days:
                return True
            else:
                return False

        def multiple_days_schedule(self):
            """
            This function sets the schedule based on the days of the week. It checks if the days are 
            Monday, Wednesday and Friday, Monday and Wednesday, or Tuesday and Thursday and sets 
            the schedule accordingly.
            """
            self.schedule = self.actual_days()
            if mwf_days(self) or mw_days(self) or tth_days(self):
                if mwf_days(self):
                    hour_arriving = random.choices(list(daily_prob.keys()),list(daily_prob.values()))[0]
                    self.schedule["Monday"] = hour_arriving
                    self.schedule["Wednesday"] = hour_arriving
                    self.schedule["Friday"] = hour_arriving
                elif mw_days(self):
                    hour_arriving = random.choices(list(daily_prob.keys()),list(daily_prob.values()))[0]
                    self.schedule["Monday"] = hour_arriving
                    self.schedule["Wednesday"] = hour_arriving
                if tth_days(self):
                    hour_arriving = random.choices(list(daily_prob.keys()),list(daily_prob.values()))[0]
                    self.schedule["Tuesday"] = hour_arriving
                    self.schedule["Thursday"] = hour_arriving
                    
            for day in self.schedule.keys():
                if self.schedule[day] == 1:
                    hour_arriving = random.choices(list(daily_prob.keys()),list(daily_prob.values()))[0]
                    self.schedule[f"{day}"] = hour_arriving

        multiple_days_schedule(self)

    def choose_hour(self):
        """
        This function returns the hour of arrival based on a probability distribution.
        """
        days_prob = {day: {0:0/14,1:0/14,2:0/14,3:0/14,4:0/14,5:1/14,6:1/14,7:7/14,8:3/14,9:7/14,10:3/14,11:7/14,12:3/14,
                            13:1/14,14:1/14,15:1/14,16:1/14,17:1/14,18:1/14,19:1/14,20:1/14,21:0/14,22:0/14,23:0/14} for day in self.actual_days()}

        self.schedule = self.actual_days()

        #Checks to see how many days were generated. 
        #If one exists, then it generated a random time for its schedule.
        if any(self.actual_days()) and len(self.actual_days()) == 1:
            chosen_day = next(iter(self.actual_days()))
            chosen_hour = random.choices(list(days_prob[chosen_day].keys()),list(days_prob[chosen_day].values()))[0]
            self.schedule[chosen_day] = chosen_hour

        #If more than one exists, then it uses a function to go through the days and set a more organized schedule    
        elif any(self.actual_days()) and len(self.actual_days()) > 1:
            self.class_time_repeating()

        #Some students never show up...    
        else:
            return None

    def hour_second_randomizer(self, day_of_week, hour_of_day):
        days_of_week = {"Sunday": 0,
                        "Monday": 86400,
                        "Tuesday": 172800,
                        "Wednesday": 259200,
                        "Thursday": 345600,
                        "Friday": 432000,
                        "Saturday": 518400}

        #Randomizes the specific second that the student will arrive.
        seconds_passed = days_of_week[day_of_week] + int(hour_of_day) * 60 * 60
        start_of_hour = seconds_passed
        end_of_hour = start_of_hour + 60 * 60 - 1
        second_of_arrival = random.randint(start_of_hour, end_of_hour)
        return(second_of_arrival)

    def arrival_time_generator(self):
        arrival = [self.hour_second_randomizer(day, self.schedule[day]) for day in self.schedule.keys()]
        self.arrival_time = arrival

    def generate_drive_speed(self):
        '''
        Is to be called when enqueued in the linked list
        Will take the attributes for speed and standard deviation to randomly generate a speed
        each time the driver is enqueued.
        '''
        todays_speed = self.speed["drive_speed"] + random.randint(-self.speed["drive_speed_var"], self.speed["drive_speed_var"])
        return todays_speed

if __name__ == "__main__":
    students = Student_Queue()
    current_driver = students.head
    while current_driver != None:
        print(current_driver.driver.arrival_time)
        current_driver = current_driver.next
