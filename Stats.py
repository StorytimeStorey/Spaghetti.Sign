class stats:

    # num signs seen vs days of attendance graph
    def format_sign_vs_attendance(self, data):
        '''
        Takes the input data and formats it to work with the create_graph function in the GUI class
        '''
        pass

    # student average num signs seen per week
    def student_avg_signs_seen(self, data: dict, weeks_run: int):
        '''
        Inputs:
            data - dict in format: {student: num signs seen}
            weeks_run - number of weeks the simulation ran
        '''
        num_students = 0
        total_signs_seen = 0
        for signs_seen in data.values(): 
            total_signs_seen += signs_seen
            num_students += 1
        average = (total_signs_seen)/(num_students)
        return average
            
    # total signs seen vs day of the week graph (y-axis: #signs seen by all student, x-axis: day of the week)
    def format_sign_vs_week_day(self, data):
        '''
        Takes the input data and formats it to work with the create_graph function in the GUI class
        '''
        pass
    # number of signs not seen
    # percent students that saw each sign, percent of student body who saw any particular sign
    # 
# 