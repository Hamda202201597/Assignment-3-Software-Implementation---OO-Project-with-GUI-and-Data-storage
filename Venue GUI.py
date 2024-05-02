import tkinter as tk
from tkinter import messagebox
import pickle
import os
class venue : #creating a class venue
    def __init__(self, venues_id, name, address, contact_details, min_guests, max_guest): #Initialiser for all The attributes pertaining to venue
        self.venues_id=venues_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.min_guests=min_guests
        self.max_guest=max_guest

    def save(self):
        with open(f'venue_{self.venues_id}.pkl', 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def load(venues_id):
        try:
            with open(f'venue_{venues_id}.pkl', 'rb') as input:
                return pickle.load(input)
        except FileNotFoundError:
            return None

class VenueGUI:
    def __init__(self,master):
        self.master=master
        master.title("Platform for venue management")

        tk.Label(master,text="venues id").grid(row=0)
        self.venues_id_entry=tk.Entry(master)
        self.venues_id_entry.grid(row=0,column=1)

        tk.Label(master, text="venues name").grid(row=1)
        self.venues_name_entry = tk.Entry(master)
        self.venues_name_entry.grid(row=1, column=1)

        tk.Label(master, text="venues address").grid(row=2)
        self.venues_address_entry = tk.Entry(master)
        self.venues_address_entry.grid(row=2, column=1)

        tk.Label(master, text="venues contact details").grid(row=3)
        self.venues_cont_entry = tk.Entry(master)
        self.venues_cont_entry.grid(row=3, column=1)

        tk.Label(master, text="venues min guests").grid(row=4)
        self.venues_min_entry = tk.Entry(master)
        self.venues_min_entry.grid(row=4, column=1)

        tk.Label(master, text="venues max guests").grid(row=5)
        self.venues_max_entry = tk.Entry(master)
        self.venues_max_entry.grid(row=5, column=1)

        self.add=tk.Button(master,text="add venue details",command=self.addvenuedetails)
        self.add.grid(row=6,column=0)

        self.display = tk.Button(master, text="display venue details", command=self.displayvenuedetails)
        self.display.grid(row=6, column=1)

    def addvenuedetails(self):
        venues_id=self.venues_id_entry.get()
        name=self.venues_name_entry.get()
        address=self.venues_address_entry.get()
        cont=self.venues_cont_entry.get()
        min=self.venues_min_entry.get()
        max=self.venues_max_entry.get()
        if all([venues_id,name,address,cont,min,max]):
            venue(venues_id,name,address,cont,min,max).save()
            messagebox.showinfo("info","all venue details have been added")
        else:
            messagebox.showerror("error","answer all the boxes")

    def displayvenuedetails(self):
        venues_id = self.venues_id_entry.get()
        venue1=venue.load(venues_id)
        if venue1:
            info=f"venues ID:{venue1.venues_id}\n Venues name: {venue1.name}\nvenues address: {venue1.address}\nvenues contact details: {venue1.contact_details}\nvenues minimum guests: {venue1.min_guests}\nvenues maximum guests: {venue1.max_guest}"
            messagebox.showinfo("Venue Details", info)
        else:
            messagebox.showerror("error","we connot find venue details")

if __name__=="__main__":
    root=tk.Tk()
    app= VenueGUI(root)
    root.mainloop()





