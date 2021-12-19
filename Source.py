import pandas as pd
import numpy as np
import os, time, re, sys
from datetime import datetime
from tkinter import filedialog
from tkinter import *


def process(huge_list):
    final_list = []
    for i in huge_list:
        dateformat = '%m/%d/%y %H:%M'
        for j in i:
            try:
                #dateformat = '%m/%d/%y %H:%M'
                x = datetime.strptime(j.split()[0].strip(',') + ' ' + j.split()[1], dateformat)
            except:
            
                print('changed date format')
                dateformat = '%d/%m/%y %H:%M'
                x = datetime.strptime(j.split()[0].strip(',') + ' ' + j.split()[1], dateformat)
                
        for j in i:
            this_date = datetime.strptime(j.split()[0].strip(',') + ' ' + j.split()[1], dateformat)    
            final_list.append([this_date, j])

    df = pd.DataFrame(final_list, columns = ['Date', 'Message'])
    df = df.drop_duplicates()
    df = df.sort_values(by = "Date", kind = 'mergesort')
    df = df.reset_index()
    return df



def main():
    file_names = []
    huge_list = []
    output_file_name = ""

    root = Tk()
    root.title('Open Files to Merge')
    label = Label(root, text = "Enter the name of your output file").pack()
    e = Entry(root, width = 40)
    e.pack()

    def openbox():
        file_names = []
        huge_list = []
        output_file_name = ""
        file_names = filedialog.askopenfilenames(initialdir = './', title = 'Open Files to Merge')
        print(file_names)
        output_file_name = e.get()
        if output_file_name == "":
            output_file_name = os.path.basename(file_names[0]).strip('.txt') + '_merged.txt'
        else:
            output_file_name = output_file_name + '.txt'

        number = len(file_names)

        for i in range(number):
            f = file_names[i]
            with open(f, 'r+', encoding = 'utf8') as File:
                lines = File.readlines()
                for l in lines[:]:
                    if '/' not in l:
                        lines.remove(l)
                    elif 'https' in l and ',' not in l:
                        lines.remove(l)
                    elif ':' not in l:
                        lines.remove(l)
                    elif 'Messages and calls are end-to-end encrypted' in l:
                        lines.remove(l)
          
            huge_list.append(lines)

        df = process(huge_list)
        final_list = []

        for i in range(len(df)):
            final_list.append(df["Message"][i])
        # print(sys.argv[1].strip('.txt') + '_merged.txt')

        with open(output_file_name, 'w', encoding = 'utf8') as File:
            File.writelines(final_list)
        l = Label(root, text = "Done!").pack()
    btn = Button(root, text="Open files to merge and Start", command=openbox).pack()

    # root.destroy()
    root.mainloop()

main()