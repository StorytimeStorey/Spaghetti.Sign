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
import pygame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class main_window:
    def __init__(self, song_list, 
                 slide_arrange_button_S_func: function, 
                 slide_arrange_button_R_func: function, 
                 run_sim: function):
        '''
        Initial main window method
        Inputs:
            song_list - list of songs, must be formatted as follows: ["song.file_type"]
            slide_arrange_button_R_func - the function to be executed when random slides is selected
            slide_arrange_button_S_func - the function to be executed when cycle slides is selected
            run_sim - the function that will be executed when the compute button is pressed, runs the simulation
        '''
        # variable for file path of the audio file to play
        self.song_list = song_list
        # create tkinter window, set size, make non-resizable
        self.window = tk.Tk()
        self.slide_arrange_button_S_func = slide_arrange_button_S_func
        self.slide_arrange_button_R_func = slide_arrange_button_R_func
        self.run_sim = run_sim
        self.window.title('Spaghetti Sign')
        self.window_width = 800
        self.window_height = 700
        self.window.geometry(f'{self.window_width}x{self.window_height}')
        self.window.resizable(width=False, height=False)
        # set a protocol for when the window is closed
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def play_audio(self, song_to_play):
        '''
        Plays the audio file input in __init__ named self.file_path
        Inputs:
            song_to_play - index of desired song from song_list
        '''
        pygame.mixer.init()
        self.file_path = self.song_list[song_to_play]
        # Load the audio file
        pygame.mixer.music.load(self.file_path)
        # Start playing the audio
        pygame.mixer.music.play()
        # continues to update the tkinter window while music is playing, keeps window responsive
        while pygame.mixer.music.get_busy():
            self.window.update()
    
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
        # To Do: place a canvas on page2, then place a frame on the canvas, then make it scrollable
        self.notebook.add(self.page1, 
                    text="Input Field")
        self.notebook.add(self.page2, 
                    text="Results")
        self.page2_canvas = tk.Canvas(self.page2)
        self.page2_canvas.place()
        self.page2_canvas_frame = tk.Frame(self.page2_canvas)
        self.page2_canvas_window = self.page2_canvas.create_window((0, 0), window=self.page2_canvas_frame)
        vertical_scroll = tk.Scrollbar(self.page2, command=self.page2_canvas.yview)
        vertical_scroll.place(relx=.5, rely=.5)
        self.page2_canvas.configure(yscrollcommand=vertical_scroll.set)
        for i in range(1, 101):
            tk.Label(self.page2_canvas_frame, text=str(i), width=5, height=2).pack()
        # activates when_selected function when the tab is changed
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
        title_label = ttk.Label(self.page1, 
                                text='SPAGHETTI SIGN PROJECT', 
                                font=("Times New Roman", 18))
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
                                                                 self.slide_arrange_button_S_func()])
        self.slide_arrange_button_S.place(relx=0.3, 
                                          rely=0.47, 
                                          anchor='nw')
        self.slide_arrange_button_R = tk.Button(self.page1, 
                                                text='Random', 
                                                width=10,
                                                foreground='gray',
                                                command=lambda: [main_window.button_selected(self, function=self.slide_arrange_button_R),
                                                             self.slide_arrange_button_S_func()])
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
        self.computer_button = ttk.Button(self.page1, text='COMPUTE', width=10, command=self.run_sim)
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

# start of testing code
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
# end testing

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