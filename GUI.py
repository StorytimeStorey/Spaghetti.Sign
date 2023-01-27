# GUI System
# Last edited 1-26-23 by Jackson & Maverick
# The GUI Lagoon

# Current Issues/To Dos:
# Make sure GUI it works with everything else.
# Add button to take all the things and do all the math mumbo jumbo.
# Make the slide arrangement button selected easier to look at.
# Say hi to the wife and kids.


import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI setup info
window = tk.Tk()
window.title('Spaghetti Sign')
window_width = 800
window_height = 700
window.geometry(f'{window_width}x{window_height}')

# TTK Notebook setup info
notebook = ttk.Notebook(window)
notebook.place(width=window_width, height=window_height)

page1 = ttk.Frame(window)
page2 = ttk.Frame(window)
page1.place(anchor='e')
page2.pack()

notebook.add(page1, 
             text="Input Field")
notebook.add(page2, 
             text="Results")


# Page 1's labels. All of them.
# Title label.
title_label = ttk.Label(page1, text='SPAGHETTI SIGN PROJECT', font=("Times New Roman", 18))
title_label = ttk.Label(page1, 
                        text='SPAGHETTI SIGN PROJECT', 
                        font=("Times New Roman", 18))
title_label.pack()

#Vehicle header Label.
vehicle_header = ttk.Label(page1, 
                           text='Vehicle Info:', 
                           font=("Arial", 20))
vehicle_header.place(relx=0.05, 
                     rely=0.1, 
                     anchor='nw')

#Vehicle number Label & Entry.
vehicle_number_label = ttk.Label(page1, 
                                 text='Number of students/cars:', 
                                 font=("Arial", 16))
vehicle_number_label.place(relx=0.055, 
                           rely=0.17, 
                           anchor='nw')

vehicle_number_entry = ttk.Entry(page1, 
                                 width=15, 
                                 font=("Times New Roman", 
                                 16))
vehicle_number_entry.place(relx=0.36, 
                           rely=0.17, 
                           anchor='nw')

#Vehicle attendance Label & Slider.
vehicle_attendance_label = ttk.Label(page1, 
                                     text='Days of attendance:', 
                                     font=("Arial", 
                                     16))
vehicle_attendance_label.place(relx=0.055,
                               rely=0.22, 
                               anchor='nw')

# vehicle_attendance_slider_value = tk.IntVar()
vehicle_attendance_variable = tk.IntVar()
vehicle_attendance_slider = tk.Scale(page1, 
                                      from_=1, 
                                      to=5, 
                                      orient='horizontal',
                                      variable=vehicle_attendance_variable,
                                      width=15,
                                      sliderlength=20)
vehicle_attendance_slider.place(relx=0.36, 
                                rely=0.22, 
                                anchor='nw')


#Sign header Label.
sign_header = ttk.Label(page1, 
                        text='Sign Info:', 
                        font=("Arial", 
                        20))
sign_header.place(relx=0.05, 
                  rely=0.3, 
                  anchor='nw')

#Slide number Label.
slide_number_label = ttk.Label(page1, 
                               text='Number of slides:', 
                               font=("Arial", 
                               16))
slide_number_label.place(relx=0.055, 
                         rely=0.37, 
                         anchor='nw')

slide_number_entry = ttk.Entry(page1, 
                               width=13, 
                               font=("Times New Roman", 
                               16))
slide_number_entry.place(relx=0.3, 
                         rely=0.37, 
                         anchor='nw')

#Slide Speed Labels & Entry.
slide_speed_label = ttk.Label(page1, 
                              text='Slide cycle speed:', 
                              font=("Arial", 16))
slide_speed_label.place(relx=0.055, 
                        rely=0.42, 
                        anchor='nw')

slide_speed_entry = ttk.Entry(page1, 
                              width=6, 
                              font=("Times New Roman", 
                              16))
slide_speed_entry.place(relx=0.3, 
                        rely=0.42, 
                        anchor='nw')

slide_speed_seconds_label = ttk.Label(page1, 
                                      text='  seconds', 
                                      font=("Arial", 
                                      14))
slide_speed_seconds_label.place(relx=0.385, 
                                rely=0.426, 
                                anchor='nw')

#Slide Arrange Label & Buttons.
slide_arrange_label = ttk.Label(page1, 
                                text='Slide arrangement:', 
                                font=("Arial", 16))
slide_arrange_label.place(relx=0.055, 
                          rely=0.47, 
                          anchor='nw')

computer_button = ttk.Button(page1, text='COMPUTE', width=10)
computer_button.place(relx=0.5, rely=0.6, anchor='n')
# change the buttons slideshow and random colors to show which is selected


def button_selected(function):
    if function is slide_arrange_button_S:
        print('trying to change slideshow')
        slide_arrange_button_S.config(highlightbackground='white')
        slide_arrange_button_R.config(highlightbackground='gray')
    elif function is slide_arrange_button_R:
        print('trying to change random')
        slide_arrange_button_R.config(highlightbackground='white')
        slide_arrange_button_S.config(highlightbackground='gray')

slide_arrange_button_S = tk.Button(page1, 
                                    text='Slideshow',
                                    width=10,
                                    command=lambda: button_selected(slide_arrange_button_S))
slide_arrange_button_S.place(relx=0.3, 
                             rely=0.47, 
                             anchor='nw')
# button_selected(slide_arrange_button_S)
slide_arrange_button_R = tk.Button(page1, 
                                    text='Random', 
                                    width=10,
                                    command=lambda: button_selected(slide_arrange_button_R))
slide_arrange_button_R.place(relx=0.474, 
                             rely=0.47, 
                             anchor='nw')

# Page 2's labels.
# test_label = ttk.Label(page2, 
#                        text='Results:', 
#                        font=("Times New Roman", 
#                        18))
# test_label.pack()

# bar graph class 
class bar_graph:

    def __init__(self, data_to_graph: dict, chart_title: str):
        '''
        Inputs: 
        x_axis_label - label of the x-axis
        y_axis_label - label of the y-axis
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
        figure1 = plt.Figure(figsize=(6, 5), dpi=100)

        # add a subplot to the figure
        ax1 = figure1.add_subplot(111)

        # create a FigureCanvasTkAgg object to display the figure in a tkinter window
        bar1 = FigureCanvasTkAgg(figure1, page2)
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
test_graph = bar_graph(data_to_graph=testing_data, chart_title='Testing chart')
            

# num signs seen vs days of attendance graph

# student average num signs seen per week

# total signs seen vs day of the week graph (y-axis: #signs seen by all student, x-axis: day of the week)


# Credit label.
credits_label = ttk.Label(window, text='Made by Story, Jack, & Maverick', font=("Arial",10))
credits_label.place(relx=0, rely=.97, anchor='nw')

window.resizable(width=False, height=False)
window.mainloop()