# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:28:42 2021

@author: Vincent
"""

'''
Goal of this code is to rename files in a directory for SWV functional maps
'''
import os
import os.path
from os import path
try:
    # if user has python2
    from Tkinter import *
    import Tkinter.font as font
    from tkFileDialog import *
except ImportError:
    # if user has python3
    from tkinter import *
    import tkinter.font as font
    import tkinter.messagebox as mb
    from tkinter import filedialog
    
root = Tk()

class Application(Frame):
    '''
    Class that contains the functions and set up for the various windows within
    the GUI.
    '''

    def __init__(self, master=None):
        '''
        Function to initialize a series of variables, including
        the size of the window, title, background image, and the welcome
        screen.

        Parameters
        ----------

        master: *operator*
            Master signifies if window will be root or tk()

        Returns
        -------

        None
        '''

        Frame.__init__(self, root)
        self.master.geometry('500x200')
        self.master.resizable(False, False)
        self.master.title('File Name')
        self.grid()
        self.screen()
    
    def screen(self):
        # set up background image
        self.canvas = Canvas(self, width=500, height=200)
        self.canvas.pack()
        self.myFont_heading = font.Font(family='Helvetica', size=20)
        self.canvas.create_text(250, 25, text= "Choose File Directory", font= self.myFont_heading)
        
        self.browse = Button(self,
                             text="Browse Files", width=15,
                             command=self.explorer_file)
        
        self.browse_c = self.canvas.create_window(190, 50,
                                                  anchor="nw",
                                                  window=self.browse)
        
        self.canvas.create_text(245, 100, text="Write New File Name",
                                font=self.myFont_heading)
        self.new_entry = StringVar()
        self.new_entry_name = Entry(self, textvariable=self.new_entry,
                                    width=30)
        new_entry_name = self.canvas.create_window(150, 130, 
                                                   anchor='nw',
                                                   window=self.new_entry_name)
        self.rename_b = Button(self,
                             text="Enter", width=10,
                             command=self.confirm)
        
        self.rename_bb = self.canvas.create_window(200, 155,
                                                  anchor="nw",
                                                  window=self.rename_b)
        
    def explorer_file(self):
        

        # opens a file explorer for the user
        self.filename = filedialog.askdirectory(initialdir="/",
                                               title="Choose a file.")

        self.files = os.listdir(self.filename)
        # print(self.files)
        self.a= sorted(self.files, key = self.last_char)
        
    def confirm(self):
        answer_txt = 'Do you want to rename all text files in this directory to "' + self.new_entry.get() + "_*.txt" +'" ?'
        answer = mb.askquestion('Confirm Folder', answer_txt)
        if answer == 'yes':
            self.rename()
        if answer == 'no':
            pass
        
    def last_char(self, x):
        return(x[-5:3])
    
    def rename(self):
        count = 1
        for i in self.a:
            if i.endswith(".txt"):
                name , extension = path.splitext(i)
                new_name = self.new_entry.get() + "_" + str(count) + extension
                before = os.path.join(self.filename, i)
                after = os.path.join(self.filename, new_name)
                os.rename(before, after)
                count += 1
                
        mb.showinfo("Success!", "Files successfully renamed!")
      
       
        
      
       
        
        
if __name__ == "__main__":
    app = Application(master=root)
    app.mainloop()






































