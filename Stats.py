class stats:

    # formatting functions
    # num signs seen vs days of attendance graph
    def format_sign_vs_attendance(self, data):
        '''
        Takes the input data in format {image: number of times seen} and formats it to work 
        with the create_graph function in the GUI class
        makes it this format: 
        {'x-axis label': [x, axis, categorical, variables], 'y-axis label': [bar value]}
        '''
        return_dict = {}
        for driver in data.keys():
            
        pass

    # total signs seen vs day of the week graph (y-axis: #signs seen by all student, x-axis: day of the week)
    def format_sign_vs_week_day(self, data):
        '''
        Takes the input data and formats it to work with the create_graph function in the GUI class
        '''
        pass

    # data analysis functions
    # student average num signs seen per week
    def student_avg_signs_seen(self, stud_signs_seen: dict, weeks_run: int):
        '''
        Returns a rounded value representing the average number of signs any given student saw on any given week
        Inputs:
            stud_signs_seen - dict in format: {student: num signs seen}
            weeks_run - number of weeks the simulation ran
        '''
        num_students = len(stud_signs_seen)
        total_signs_seen = 0
        for signs_seen in stud_signs_seen.values(): 
            total_signs_seen += signs_seen
        average = (total_signs_seen)/(num_students)
        average_per_week = round(average/weeks_run)
        return average_per_week
            
    # average number of signs not seen per week
    def signs_not_seen(self, stud_signs_seen: dict, weeks_run: int, num_signs: int):
        '''
        Returns a rounded value representing the average number of signs any given student in any given week did not see
        Inputs:
            stud_signs_seen - dict in format: {student: num signs seen}
            weeks_run - number of weeks the simulation ran
            num_signs - number of images cycling through the sign
        '''
        average = self.student_avg_signs_seen(stud_signs_seen, weeks_run)
        signs_not_seen = round((num_signs)-(average))
        return signs_not_seen
        
    # percent students that saw each sign, percent of student body who saw any particular sign
    def chance_seen(self, num_students: int, num_students_viewed: dict):
        '''
        Returns a proportion representing the chance that any given student would see any given sign in any given week
        Inputs: 
            num_signs - number of images cycling through the sign
            num_students - number of students who could have seen any sign
            num_students_viewed - dict in format {sign_image: number of students who saw that image}
        '''
        # find average number of signs students see per week
        stud_seen_list = []
        for students in num_students_viewed.values():
            proportion_saw = students/num_students
            stud_seen_list.append(proportion_saw)
        average_proportion = round((sum(stud_seen_list))/(len(stud_seen_list)), 4)
        return average_proportion