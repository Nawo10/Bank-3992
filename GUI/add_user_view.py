import tkinter as tk
from gui_configuration import Button, Frame, Label


class AddUserView(Frame):
    '''
    this Frame collects new data and send them back to main.py via callback()
    callback1 will close tab after clicking btn submit.
    callback2 to show err
    '''
    
    def __init__(self, master = None, callback = None,
                                      callback1 = None,
                                      callback2 = None):
        super().__init__(master)
        self.callback = callback  # add_employee()
        self.callback1 = callback1  # close_tab()
        self.callback2 = callback2  # show_err()
        self.pack(expand = True)
        
        # Defining widgets
        self.lbl_name = Label(self, text = "Name:")
        self.lbl_name.grid(row = 0, column = 0,
                           padx = 10, pady = 10, sticky = "w")  
        self.lbl_id = Label(self, text = "ID:")
        self.lbl_id.grid(row = 1, column = 0,
                         padx = 10, pady = 10, sticky = "w")
        self.lbl_username = Label(self, text = "Username:")
        self.lbl_username.grid(row = 2, column = 0,
                               padx = 10, pady = 10, sticky = "w")        
        self.lbl_pass = Label(self, text = "Password:")
        self.lbl_pass.grid(row = 3, column = 0,
                           padx = 10, pady = 10, sticky = "w")
        
        self.ent_name = tk.Entry(self)
        self.ent_name.grid(row = 0, column = 1)
        self.ent_id = tk.Entry(self)
        self.ent_id.grid(row = 1, column = 1)
        self.ent_username = tk.Entry(self)
        self.ent_username.grid(row = 2, column = 1)
        self.ent_pass = tk.Entry(self, show = "*")
        self.ent_pass.grid(row = 3, column = 1)
        
        self.btn_submit = Button(self, text = "Submit",
                                    command = self.submit)
        self.btn_submit.grid(row = 4, column = 0, columnspan = 2,
                             padx = 10, pady = 10)
        
        self.ent_name.focus_set()
        
        # press Enter to go next, stop clickin!
        self.entries = [ent for ent in self.winfo_children()
                        if isinstance(ent, tk.Entry)]
        self.ent_name.bind("<Return>",
                               lambda _: self.entries[1].focus_set())
        self.ent_id.bind("<Return>",
                               lambda _: self.entries[2].focus_set())
        self.ent_username.bind("<Return>",
                               lambda _: self.entries[3].focus_set())        
        self.ent_pass.bind("<Return>", lambda _: self.btn_submit.invoke())
        
    def submit(self):
        data = self.return_data()
        if self.callback:  
            result = self.callback(*data)  # sending data to main.py
            self.clear()
            if isinstance(result, str):  # means an error occured
                if self.callback2:
                    self.callback2("Error", result)
            else:
                if self.callback1:  # = if no err occured then close the tab.
                    self.callback1()
                
    def return_data(self):
        new_name = self.ent_name.get()
        new_id = self.ent_id.get()
        new_username = self.ent_username.get()
        new_pass = self.ent_pass.get()
        new_data = (new_name, new_username, new_id, new_pass)
        if all(item.isalnum() for item in new_data):
            return new_data
        
    def clear(self):
        self.ent_name.delete(0, tk.END)
        self.ent_id.delete(0, tk.END)
        self.ent_username.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)
   
if __name__ == "__main__":
    win = tk.Tk()
    fr = AddUserView(win)
    win.mainloop()
    