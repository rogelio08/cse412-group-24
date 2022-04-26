# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
# from tkinter.ttk import *
import tkinter
import csv

# creates a Tk() object
master = Tk()

# open up the counties csv file and turn it into usable data
with open('us-counties-recent-modded.csv', newline='') as f:
    reader = csv.reader(f)
    co_data = list(reader)

# open up the colleges csv file and turn it into usable data
with open('colleges-modded.csv', newline='') as f:
    reader = csv.reader(f)
    college_data = list(reader)

# open up the mask use csv file and turn it into usable data
with open('mask-use-by-county.csv', newline='') as f:
    reader = csv.reader(f)
    mask_data = list(reader)

# open up the state csv file and turn it into usable data
with open('us-states-modded.csv', newline='') as f:
    reader = csv.reader(f)
    state_data = list(reader)

# sets the geometry of main
# root window
master.geometry("500x500")

print(co_data[1])
print(co_data[1][4])
user_pref = 0
list_of_fips_vio = []

# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    # A Label widget to show in toplevel
    Label(newWindow, text="This is a new window").pack()

    Label(newWindow, text=co_data[1][0]).pack()


def get_user_preferences():
    global user_pref
    global list_of_fips_vio
    list_of_fips_vio.clear()

    user_preference = preferences_input_box.get(1.0, "end-1c")
    user_pref = user_preference
    for values in range(len(co_data)):
        if co_data[values][4].isnumeric() and (int(co_data[values][4]) > int(user_pref)) and co_data[values][3] not in list_of_fips_vio:
            list_of_fips_vio.append(co_data[values][3])
    curr_pref_label.config(text="Current preferences are: " + user_preference + " " + list_of_fips_vio[0])

# function to open a new window for county information
# on a button click
def open_new_county_window():
    # Toplevel object which will
    # be treated as a new window
    new_county_window = Toplevel(master)
    global user_pref

    # sets the title of the
    # Toplevel widget
    new_county_window.title("New County Window")

    # sets the geometry of toplevel
    new_county_window.geometry("400x400")

    # A Label widget to show in toplevel
    Label(new_county_window, text="This is a new window for the covid-19 case and death numbers per county").pack()

    listbox = Listbox(new_county_window)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)

    # create a scrollbar to contain all the info from the csv files
    scrollbar = Scrollbar(new_county_window)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.insert(END, co_data[0])
    for values in range(1, len(co_data)):
        if co_data[values][4] in list_of_fips_vio:
            listbox.insert(END, co_data[values])
#        if co_data[values][4].isnumeric() and (int(co_data[values][4]) > int(user_pref)):
#            listbox.insert(END, co_data[values])

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Label(new_county_window, text=co_data).pack()


# function to open a new window for college information
# on a button click
def open_new_college_window():
    # Toplevel object which will
    # be treated as a new window
    new_college_window = Toplevel(master)
    global user_pref

    # sets the title of the
    # Toplevel widget
    new_college_window.title("New College Window")

    # sets the geometry of toplevel
    new_college_window.geometry("400x400")

    # A Label widget to show in toplevel
    Label(new_college_window, text="This is a new window for the covid-19 case and death numbers per county").pack()

    listbox = Listbox(new_college_window)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)

    # create a scrollbar to contain all the info from the csv files
    scrollbar = Scrollbar(new_college_window)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.insert(END, college_data[0])
    for values in range(1, len(college_data)):
        if college_data[values][6].isnumeric() and (int(college_data[values][6]) > int(user_pref)):
            listbox.insert(END, college_data[values])

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    # Label(new_county_window, text=co_data).pack()


# function to open a new window for mask use information
# on a button click
def open_new_mask_use_window():
    # Toplevel object which will
    # be treated as a new window
    new_mask_window = Toplevel(master)
    global user_pref

    # sets the title of the
    # Toplevel widget
    new_mask_window.title("New Mask Use Window")

    # sets the geometry of toplevel
    new_mask_window.geometry("400x600")

    # A Label widget to show in toplevel
    Label(new_mask_window, text="This is a new window for the mask usage percentages of counties that violate preferences").pack()

    listbox = Listbox(new_mask_window)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)

    # create a scrollbar to contain all the info from the csv files
    scrollbar = Scrollbar(new_mask_window)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.insert(END, mask_data[0])
    for values in range(1, len(mask_data)):
        if mask_data[values][0] in list_of_fips_vio:
            listbox.insert(END, mask_data[values])

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    # Label(new_county_window, text=co_data).pack()


# function to open a new window for state information
# on a button click
def open_new_state_window():
    # Toplevel object which will
    # be treated as a new window
    new_state_window = Toplevel(master)
    global user_pref

    # sets the title of the
    # Toplevel widget
    new_state_window.title("New State Window")

    # sets the geometry of toplevel
    new_state_window.geometry("400x400")

    # A Label widget to show in toplevel
    Label(new_state_window, text="This is a new window for the covid-19 case and death numbers per US state").pack()

    listbox = Listbox(new_state_window)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)

    # create a scrollbar to contain all the info from the csv files
    scrollbar = Scrollbar(new_state_window)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox.insert(END, state_data[0])
    for values in range(1, len(state_data)):
        if state_data[values][3].isnumeric() and (int(state_data[values][3]) > int(user_pref)):
            listbox.insert(END, state_data[values])

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    # Label(new_county_window, text=co_data).pack()


label = Label(master, text="This is the main window")
label.pack(pady=10)

preference_frame = Frame(master, bg="black")
preference_frame.pack(side=TOP, anchor=NW, padx=15, pady=15)

preferences_label = Label(preference_frame, text="Please enter your preferences regarding covid cases:")
preferences_label.pack(side=TOP, anchor=NE, padx=15, pady=15)

preferences_input_box = Text(preference_frame, height=2, width=10)
preferences_input_box.pack(pady=0)

preferences_button = Button(preference_frame, text="Set preferences", command=get_user_preferences)
preferences_button.pack(pady=15)

curr_pref_label = Label(preference_frame, text="No preferences entered yet")
curr_pref_label.pack(pady=(0, 15))

# a button widget which will open a
# new window on button click
btn = Button(master, text="Click to open a new window", command=openNewWindow)
btn2 = Button(master, text="View data per county", command=open_new_county_window)
# btn.pack(pady=10)
btn.pack(side=tkinter.TOP, anchor=NW, padx=15, pady=15)
btn2.pack(side=TOP, anchor=NW, padx=15, pady=0)

col_btn = Button(master, text="View data per US college", command=open_new_college_window)
col_btn.pack(side=TOP, anchor=NW, padx=15, pady=15)

mask_btn = Button(master, text="View mask use in violating counties", command=open_new_mask_use_window)
mask_btn.pack(side=TOP, anchor=NW, padx=15, pady=(0, 15))

state_btn = Button(master, text="View data per US state", command=open_new_state_window)
state_btn.pack(side=TOP, anchor=NW, padx=15, pady=(0, 15))

# mainloop, runs infinitely
mainloop()
