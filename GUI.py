import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Spaghetti Sign')
window_width = 800
window_height = 700
window.geometry(f'{window_width}x{window_height}')

notebook = ttk.Notebook(window)
notebook.pack()

page1 = ttk.Frame(window)
page2 = ttk.Frame(window)
page1.pack()
page2.pack()

notebook.add(page1, text="Input Field")
notebook.add(page2, text="Results")



# title_label = tk.Label(window, text='SPAGHETTI SIGN PROJECT', font=("Times New Roman", 18))
# title_label.pack()

# vehicle_header = tk.Label(window, text='Vehicle Info:', font=("Arial", 20))
# vehicle_header.place(relx=0.06, rely=0.1, anchor='nw')

# vehicle_number_label = tk.Label(window, text='Number of students/cars:', font=("Arial", 16))
# vehicle_number_label.place(relx=0.05, rely=0.17, anchor='nw')

# vehicle_attendance_label = tk.Label(window, text='Days of attendance:', font=("Arial", 16))
# vehicle_attendance_label.place(relx=0.05, rely=0.22, anchor='nw')

# sign_header = tk.Label(window, text='Sign Info:', font=("Arial", 20))
# sign_header.place(relx=0.06, rely=0.3, anchor='nw')

# slide_number = tk.Label(window, text='Number of slides:', font=("Arial", 16))
# slide_number.place(relx=0.05, rely=0.37, anchor='nw')

# slide_speed = tk.Label(window, text='Slide cycle speed:', font=("Arial", 16))
# slide_speed.place(relx=0.05, rely=0.41, anchor='nw')

# slide_arrange = tk.Label(window, text='Slide arrangement', font=("Arial", 16))
# slide_arrange.place(relx=0.05, rely=0.45, anchor='nw')




window.mainloop()