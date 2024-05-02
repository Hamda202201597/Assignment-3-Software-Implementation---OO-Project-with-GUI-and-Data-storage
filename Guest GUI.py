import tkinter as tk
from tkinter import messagebox
import pickle
import os

class guest1 :#creating class guest
    def __init__(self,guest_id, name, address, contact_details): #Initialiser for all The attributes pertaining to guest
        self.guest_id=guest_id
        self.name=name
        self.address=address
        self.contact_details=contact_details

    def save(self):
        with open(f'guest_{self.guest_id}.pkl','wb')as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def load(guest_id):
        try:
            with open(f'guest_{guest_id}.pkl', 'rb') as input:
                return pickle.load(input)
        except FileNotFoundError:
            return None

    def delet(self):
        os.remove(f'guest_{self.guest_id}.pkl')

class guestmanagmentgui: #starting the gui for all the system requirments
    def __init__(self,master):
        self.master = master
        master.title("Platform for guest management")

    # adding all the lables and boxes for the client attributes
        tk.Label(master, text="Guests id:").grid(row=0)
        self.guest_id_entry=tk.Entry(master)
        self.guest_id_entry.grid(row=0,column=1)

        tk.Label(master, text="Guests name:").grid(row=1)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        tk.Label(master, text="Guests address:").grid(row=2)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=2, column=1)

        tk.Label(master, text="Guests contacts details:").grid(row=3)
        self.contact_details_entry = tk.Entry(master)
        self.contact_details_entry.grid(row=3, column=1)

        # adding the buttons
        self.addguestsdetails_button=tk.Button(master, text="Add guets details",command=self.add_gusetdetails)
        self.addguestsdetails_button.grid(row=4,column=0)

        self.modifyguestdetails_button=tk.Button(master, text="modify guests details",command=self.modify_guestsdetails)
        self.modifyguestdetails_button.grid(row=4,column=1)

        self.deletguestdetails_button = tk.Button(master, text="delete guests details",command=self.delete_guestsdetails)
        self.deletguestdetails_button.grid(row=5, column=0)

        self.displayguestdetails_button = tk.Button(master, text="diplay guests details",command=self.display_guestsdetails)
        self.displayguestdetails_button.grid(row=5, column=1)


    def add_gusetdetails(self):
        guest_id=self.guest_id_entry.get()
        name=self.name_entry.get()
        address=self.address_entry.get()
        contact_details=self.contact_details_entry.get()
        if all([guest_id,name,address,contact_details]):
            guest1(guest_id,name,address,contact_details).save()
            messagebox.showinfo("info","guest details have been added")
        else:
            messagebox.showerror("error","missing information")

    def modify_guestsdetails(self):
        guest_id=self.guest_id_entry.get()
        guest=guest1.load(guest_id)
        if guest:
            guest.name=self.name_entry.get()
            guest.address=self.address_entry.get()
            guest.contact_details=self.contact_details_entry.get()
            guest.save()
            messagebox.showinfo("info","guest details have been modified")
        else:
            messagebox.showerror("error","we cannot find guest info")

    def delete_guestsdetails(self):
        guest_id=self.guest_id_entry.get()
        guest=guest1.load(guest_id)
        if guest:
            guest.delete()
            messagebox.showinfo("info", "guest details have been deleted")
        else:
            messagebox.showerror("error", "we cannot find guest info")


    def display_guestsdetails(self):
        guest_id = self.guest_id_entry.get()
        guest = guest1.load(guest_id)
        if guest:
            info = f"guests id number: {guest.guest_id}\nguests name: {guest.name}\n guests address: {guest.address}\nguests contact Details: {guest.contact_details}"
            messagebox.showinfo("guest details", info)
        else:
            messagebox.showerror("error", "we cannot find guest info")

if __name__ == "__main__":
    root = tk.Tk()
    app =guestmanagmentgui (root)
    root.mainloop()





