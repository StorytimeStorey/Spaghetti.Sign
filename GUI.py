# GUI System/Master File
# Last edited 2-2-23 by Jackson & Maverick
# The GUI Lagoon

# Current Issues/To Dos:
# Get system to check if any drivers are arriving at the current second.
# Fix audio system/errors occurring from audio.

# Make sure GUI it works with everything else.
# Say hi to the wife and kids.


import tkinter as tk
from tkinter import ttk
# import playsound
# import pygame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sign_class_finished as SC
import Driver_Class as DriverC
import Timekeeping as TimeK



class main_window:
    def __init__(self, song_list):
        '''
        Initial main window method
        Inputs:
            song_list - list of songs, must be formatted as follows: ["song.file_type"]
        '''
        # variable for file path of the audio file to play
        self.song_list = song_list
        # create tkinter window, set size, make non-resizable
        self.window = tk.Tk()
        self.window.title('Spaghetti Sign')
        self.window_width = 800
        self.window_height = 700
        self.window.geometry(f'{self.window_width}x{self.window_height}')
        self.window.resizable(width=False, height=False)
        # set a protocol for when the window is closed
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        # pygame.mixer.init()

    # def play_audio(self, song_to_play):
    #     '''
    #     Plays the audio file input in __init__ named self.file_path
    #     Inputs:
    #         song_to_play - index of desired song from song_list
    #     '''
    #     self.file_path = self.song_list[song_to_play]
    #     # Load the audio file
    #     pygame.mixer.music.load(self.file_path)
    #     # Start playing the audio
    #     pygame.mixer.music.play()
    #     # continues to update the tkinter window while music is playing, keeps window responsive
    #     while pygame.mixer.music.get_busy():
    #         self.window.update()
    
    def on_closing(self):
        '''
        destroys the tkinter window, destroys all widgets currently running when window closes
        '''
        # pygame.mixer.music.stop()
        self.window.destroy()

    # TTK Notebook setup info
    def ttk_notebook(self):
        '''
        Creates pages 1 and 2 and adds them to the window
        '''
        self.notebook = ttk.Notebook(self.window)
        self.notebook.place(width=self.window_width, height=self.window_height)

        self.page1 = ttk.Frame(self.window)
        self.page2 = ttk.Frame(self.window)
        self.page1.place(anchor='e')
        self.page2.pack()

        self.notebook.add(self.page1, 
                    text="Input Field")
        self.notebook.add(self.page2, 
                    text="Results")

        self.notebook.bind('<<NotebookTabChanged>>', self.when_selected)

    def when_selected(self, event):
        '''
        Plays an audio file when Results tab is selected
        '''
        # finds which tab is currently selected and sets this variable to the text attribute of that tab
        self.selected_tab = self.notebook.tab(event.widget.select(), 'text')
        # plays desired audio file if the selected tab is the Results tab
        if self.selected_tab == 'Results':
            self.play_audio(2)

    # Page 1's labels
    def title_label(self):
        '''
        Creates and packs the title label
        '''
        title_label = ttk.Label(self.page1, text='SPAGHETTI SIGN PROJECT', font=("Times New Roman", 18))
        title_label = ttk.Label(self.page1, 
                                text='SPAGHETTI SIGN PROJECT', 
                                font=("Times New Roman", 18))
        title_label.pack()

    def vehicle_header(self):
        '''
        Creates and places the vehicle header
        '''
        self.vehicle_header = ttk.Label(self.page1, 
                                text='Vehicle Info:', 
                                font=("Arial", 20))
        self.vehicle_header.place(relx=0.05, 
                            rely=0.1, 
                            anchor='nw')

    def vehicle_number(self):
        '''
        Creates and places the entry and label for number of students and cars
        '''
        self.vehicle_number_label = ttk.Label(self.page1, 
                                        text='Number of students/cars:', 
                                        font=("Arial", 16))
        self.vehicle_number_label.place(relx=0.055, 
                                rely=0.17, 
                                anchor='nw')

        self.vehicle_number_entry = ttk.Entry(self.page1, 
                                        width=15, 
                                        font=("Times New Roman", 
                                        16))
        self.vehicle_number_entry.place(relx=0.36, 
                                rely=0.17, 
                                anchor='nw')

    def vehicle_attendance(self):
        '''
        Creates and places the days of attendance slider and label
        '''
        self.vehicle_attendance_label = ttk.Label(self.page1, 
                                            text='Days of attendance:', 
                                            font=("Arial", 
                                            16))
        self.vehicle_attendance_label.place(relx=0.055,
                                    rely=0.22, 
                                    anchor='nw')

        self.vehicle_attendance_variable = tk.IntVar()
        self.vehicle_attendance_slider = tk.Scale(self.page1, 
                                            from_=1, 
                                            to=5, 
                                            orient='horizontal',
                                            variable=self.vehicle_attendance_variable,
                                            width=15,
                                            sliderlength=20)
        self.vehicle_attendance_slider.place(relx=0.36, 
                                        rely=0.22, 
                                        anchor='nw')

    def sign_header(self):
        '''
        Creates and places all the input information for the sign
        '''
        self.sign_header = ttk.Label(self.page1, 
                                text='Sign Info:', 
                                font=("Arial", 
                                20))
        self.sign_header.place(relx=0.05, 
                        rely=0.3, 
                        anchor='nw')

        # input for number of slides in the sign
        self.slide_number_label = ttk.Label(self.page1, 
                                    text='Number of slides:', 
                                    font=("Arial", 
                                    16))
        self.slide_number_label.place(relx=0.055, 
                                rely=0.37, 
                                anchor='nw')

        self.slide_number_entry = ttk.Entry(self.page1, 
                                    width=13, 
                                    font=("Times New Roman", 
                                    16))
        self.slide_number_entry.place(relx=0.3, 
                                rely=0.37, 
                                anchor='nw')

        # input for setting the cycle speed of the sign
        self.slide_speed_label = ttk.Label(self.page1, 
                                    text='Slide cycle speed:', 
                                    font=("Arial", 16))
        self.slide_speed_label.place(relx=0.055, 
                                rely=0.42, 
                                anchor='nw')

        self.slide_speed_entry = ttk.Entry(self.page1, 
                                    width=6, 
                                    font=("Times New Roman", 
                                    16))
        self.slide_speed_entry.place(relx=0.3, 
                                rely=0.42, 
                                anchor='nw')
        # shows units of time for cycle speed
        self.slide_speed_seconds_label = ttk.Label(self.page1, 
                                            text='  seconds', 
                                            font=("Arial", 
                                            14))
        self.slide_speed_seconds_label.place(relx=0.385, 
                                        rely=0.426, 
                                        anchor='nw')

    def slide_arrangement(self):
        '''
        creates and places the buttons to determine whether the sign cycles randomly or not
        '''
        self.slide_arrange_label = ttk.Label(self.page1, 
                                        text='Slide arrangement:', 
                                        font=("Arial", 16))
        self.slide_arrange_label.place(relx=0.055, 
                                rely=0.47, 
                                anchor='nw')
        # determines if the sign goes in an order or randomizes the images
        self.slide_arrange_button_S = tk.Button(self.page1, 
                                            text='Slideshow',
                                            width=10,
                                            foreground='gray',
                                            command=lambda: [main_window.button_selected(self, function=self.slide_arrange_button_S),
                                                            main_window.play_audio(self, 2)])
        self.slide_arrange_button_S.place(relx=0.3, 
                                    rely=0.47, 
                                    anchor='nw')
        self.slide_arrange_button_R = tk.Button(self.page1, 
                                            text='Random', 
                                            width=10,
                                            foreground='gray',
                                            command=lambda: main_window.button_selected(self, function=self.slide_arrange_button_R))
        self.slide_arrange_button_R.place(relx=0.474, 
                                    rely=0.47, 
                                    anchor='nw')

    def button_selected(self, function):
        '''
        change the slideshow and random buttons colors to show which is selected
        '''
        if function is self.slide_arrange_button_S:
            self.slide_arrange_button_S.config(foreground='black')
            self.slide_arrange_button_R.config(foreground='gray')
        elif function is self.slide_arrange_button_R:
            self.slide_arrange_button_R.config(foreground='black')
            self.slide_arrange_button_S.config(foreground='gray')

    def credit(self):
        '''
        Places the credit label
        '''
        credits_label = ttk.Label(self.window, text='Made by Story, Jack, & Maverick', font=("Arial",10))
        credits_label.place(relx=0, rely=.97, anchor='nw')

    def compute_button(self):
        '''
        Activates the simulation (not done yet)
        '''
        self.computer_button = ttk.Button(self.page1, text='COMPUTE', width=10)
        self.computer_button.place(relx=0.5, rely=0.6, anchor='n')
    
    def place_graphs(self, graph_list):
        '''
        places the graphs
        '''
        row = 0
        column = 0
        for graph in graph_list:
            graph = FigureCanvasTkAgg()
            graph.get_tk_widget().grid(row=row, column=column)
            column += 1
            if column == 2:
                column = 0
                row += 1
    
    def create_graphs(self, data_list: list, chart_title: str, desired_page):
        '''
        Inputs: 
        x_axis_label - label of the x-axis
        y_axis_label - label of the y-axis
        desired_page - the page to add the bar graph to
        chart_title - title of the bar graph
        data_to_graph - dictionary in format {'x-axis label': [x, axis, categorical, variables], 
                                                'y-axis label': [bar value]}
        '''
        row = 0
        column = 0
        # loop to create and .grid bar graphs
        for data_to_graph in data_list:
            column += 1
            self.x_axis_label = list(data_to_graph.keys())[0]
            self.y_axis_label = list(data_to_graph.keys())[1]
            self.chart_title = chart_title
            self.data_to_graph = data_to_graph
            self.data_to_graph_data_frame = pd.DataFrame(data_to_graph)
            # create a figure with a specific size and resolution
            figure1 = plt.Figure(figsize=(3.68, 4), dpi=100)

            # add a subplot to the figure
            ax1 = figure1.add_subplot(111)

            # create a FigureCanvasTkAgg object to display the figure in a tkinter window
            bar1 = FigureCanvasTkAgg(figure1, desired_page)
            bar1.get_tk_widget().grid(row=row, column=column, padx=2, pady=2)

            # group the dataframe by 'country' and sum the 'gdp_per_capita' column
            self.data_to_graph_data_frame = self.data_to_graph_data_frame[[self.x_axis_label, self.y_axis_label]].groupby(self.x_axis_label).sum()

            # plot the data on the subplot as a bar chart with a legend
            self.data_to_graph_data_frame.plot(kind='bar', legend=True, ax=ax1)

            # set the title of the subplot
            ax1.set_title(chart_title)
            if column == 2:
                column = 0
                row += 1
        
    def scroll_bar(self):
        '''
        
        '''
        scroll = tk.Scrollbar(self.page2)
        scroll.place(relx=.97, rely=.5)

        scroll.config(command=self.page2.yview)

    def main_loop(self):
        '''
        Activates the main loop
        '''
        self.window.mainloop()

# Page 2's labels.
class bar_graph:

    def __init__(self, data_to_graph: dict, chart_title: str, desired_page):
        '''
        Inputs: 
        x_axis_label - label of the x-axis
        y_axis_label - label of the y-axis
        desired_page - the page to add the bar graph to
        chart_title - title of the bar graph
        data_to_graph - dictionary in format {'x-axis label': [x, axis, categorical, variables], 
                                                'y-axis label': [bar value]}
        '''
        self.x_axis_label = list(data_to_graph.keys())[0]
        self.y_axis_label = list(data_to_graph.keys())[1]
        self.chart_title = chart_title
        self.data_to_graph = data_to_graph
        self.data_to_graph_data_frame = pd.DataFrame(data_to_graph)
        # create a figure with a specific size and resolution
        figure1 = plt.Figure(figsize=(.2, .1), dpi=100)

        # add a subplot to the figure
        ax1 = figure1.add_subplot(111)

        # create a FigureCanvasTkAgg object to display the figure in a tkinter window
        bar1 = FigureCanvasTkAgg(figure1, desired_page)
        bar1.get_tk_widget().grid(row=0, column=0)

        # group the dataframe by 'country' and sum the 'gdp_per_capita' column
        self.data_to_graph_data_frame = self.data_to_graph_data_frame[[self.x_axis_label, self.y_axis_label]].groupby(self.x_axis_label).sum()

        # plot the data on the subplot as a bar chart with a legend
        self.data_to_graph_data_frame.plot(kind='bar', legend=True, ax=ax1)

        # set the title of the subplot
        ax1.set_title(chart_title)

testing_data = {'Days of Attendance': [1, 2, 3, 4, 5],
         'Number of Signs Seen': [1, 2, 3, 4, 5]
         }
testing_data2 = {'Days of Attendance': [1, 2, 3, 4, 5],
         'Number of Signs Seen': [1, 2, 3, 4, 5]
         }
testing_data3 = {'Days of Attendance': [1, 2, 3, 4, 5],
         'Number of Signs Seen': [1, 2, 3, 4, 5]
         }
testing_data4 = {'Days of Attendance': [1, 2, 3, 4, 5],
         'Number of Signs Seen': [1, 2, 3, 4, 5]
         }
testing_data_list = [testing_data, testing_data2, testing_data3, testing_data4]

# test_graph1 = bar_graph(data_to_graph=testing_data, chart_title='Testing chart', desired_page=tkinter_window.page2)

# test_graph2 = bar_graph(data_to_graph=testing_data, chart_title='Testing chart', desired_page=tkinter_window.page2)

# test_graph3 = bar_graph(data_to_graph=testing_data, chart_title='Testing chart', desired_page=tkinter_window.page2)

# test_graph4 = bar_graph(data_to_graph=testing_data, chart_title='Testing chart', desired_page=tkinter_window.page2)

# test_graph_list = [test_graph1, test_graph2, test_graph3, test_graph4]
            
# things to add

# num signs seen vs days of attendance graph

# student average num signs seen per week

# total signs seen vs day of the week graph (y-axis: #signs seen by all student, x-axis: day of the week)

songs_list = ["I'm a Lady.flac", "Blur_Song_2.wav", "Look at this graph.flac"]
def run_gui():
    tkinter_window = main_window(songs_list)
    tkinter_window.ttk_notebook()
    tkinter_window.title_label()
    tkinter_window.vehicle_header()
    tkinter_window.vehicle_number()
    tkinter_window.vehicle_attendance()
    tkinter_window.sign_header()
    tkinter_window.slide_arrangement()
    tkinter_window.credit()
    tkinter_window.compute_button()
    tkinter_window.create_graphs(data_list=testing_data_list, chart_title='Testing', desired_page=tkinter_window.page2)
    # tkinter_window.scroll_bar()
    tkinter_window.main_loop()

run_gui()

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
    current_driver = current_driver
    drive_speed = drive_speed
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

DriverC.amount_of_students = simulated_drivers_number
print(DriverC.amount_of_students)
