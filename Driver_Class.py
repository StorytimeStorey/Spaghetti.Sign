import random

Day_List = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

Attendance_average = 2.6




class Driver:
    def __init__(self, ID, Attendance_average):
        self.ID = ID
        self.attendance_average = Attendance_average
        self.days_attending = self.days_attended()
        self.hour_arrived = self.choose_hour()
        self.data = {}

    def update_data(self, message):
        """
        This function updates the data dictionary.
        If the message is already in the data, the count is incremented.
        Otherwise, the message is added to the data with a count of 1.
        """
        if message in self.data:
            self.data[message] += 1
        else:
            self.data[message] = 1 
        
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
        hourly_prob = {0:0/14,1:0/14,2:0/14,3:0/14,4:0/14,5:1/14,6:1/14,7:7/14,8:3/14,9:7/14,10:3/14,11:7/14,12:3/14,13:1/14,14:1/14,15:1/14,16:1/14,17:1/14,18:1/14,19:1/14,20:1/14,21:0/14,22:0/14,23:0/14}
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
            self.schedule = self.actual_days()
            print(self.schedule)
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
                if self.schedule[day] is 1:
                    hour_arriving = random.choices(list(daily_prob.keys()),list(daily_prob.values()))[0]
                    print("hour arriving is" ,  hour_arriving)
                    self.schedule[f"{day}"] = hour_arriving

        multiple_days_schedule(self)


    def choose_hour(self):
        """
        This function returns the hour of arrival based on a probability distribution.
        """
        days_prob = {day: {0:0/14,1:0/14,2:0/14,3:0/14,4:0/14,5:1/14,6:1/14,7:7/14,8:3/14,9:7/14,10:3/14,11:7/14,12:3/14,
                13:1/14,14:1/14,15:1/14,16:1/14,17:1/14,18:1/14,19:1/14,20:1/14,21:0/14,22:0/14,23:0/14} for day in self.actual_days()}

        self.schedule = self.actual_days()

        if any(self.actual_days()) and len(self.actual_days()) == 1:
            chosen_day = next(iter(self.actual_days()))
            chosen_hour = random.choices(list(days_prob[chosen_day].keys()),list(days_prob[chosen_day].values()))[0]
            self.schedule[chosen_day] = chosen_hour
        elif any(self.actual_days()) and len(self.actual_days()) > 1:
            self.class_time_repeating()
        else:
            return None

drivers = [Driver(f'Driver {i}', Attendance_average) for i in range(100)]

for driver in drivers:
    print(driver.schedule)
