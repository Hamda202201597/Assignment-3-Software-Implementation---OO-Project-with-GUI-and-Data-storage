import tkinter as tk
from tkinter import messagebox
import pickle
import os

class client1 : #creating a class for the client
    def __init__(self,client_id,name,address,contact_details,budget): #Initialiser for all The attributes pertaining to client
        self.client_id=client_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.budget=budget

    def save(self): #saving the class to a file
        with open(f'client_{self.client_id}.pkl','wb') as output :
            pickle.dump(self,output,pickle.HIGHEST_PROTOCOL)

    def load(client_id): # loading and returning a client object from the file
        try:
            with open(f'client_{client_id}.pkl','rb') as input:
                return pickle.load(input)
        except FileNotFoundError :
            return None
    def delet(self):#deleteing the file that has the pickle
        os.remove(f'client_{self.client_id}.pkl')

class Clientsystem: #starting the gui for all the system requirments
    def __init__(self,master):
        self.master=master
        master.title("platform for client managment")

        #adding all the lables and boxes for the client attributes
        tk.Label(master,text='Clients ID number:').grid(row=0)
        self.client_id_entry=tk.Entry(master)
        self.client_id_entry.grid(row=0,column=1)

        tk.Label(master, text='Clients Name:').grid(row=1)
        self.client_name_entry = tk.Entry(master)
        self.client_name_entry.grid(row=1, column=1)

        tk.Label(master, text='Clients address:').grid(row=2)
        self.client_adress_entry = tk.Entry(master)
        self.client_adress_entry.grid(row=2, column=1)

        tk.Label(master, text='Clients contact information:').grid(row=3)
        self.client_contact_details_entry = tk.Entry(master)
        self.client_contact_details_entry.grid(row=3, column=1)

        tk.Label(master, text='Clients budget:').grid(row=4)
        self.client_budget_details_entry = tk.Entry(master)
        self.client_budget_details_entry.grid(row=4, column=1)

        #adding the buttons

        self.add=tk.Button(master, text="add clients details",command=self.addclientdetails)
        self.add.grid(row=5, column=0)

        self.modify=tk.Button(master,text="modify clients details",command=self.modifyclinetsdetails)
        self.modify.grid(row=5,column=1)

        self.delet = tk.Button(master, text="delete clients details", command=self.deleteclinetsdetails)
        self.delet.grid(row=6, column=0)

        self.display = tk.Button(master, text="display clients details", command=self.displayclinetsdetails)
        self.display.grid(row=6, column=1)

    def addclientdetails(self): #This define function is for colleting input from the user and savinf it all
        client_id=self.client_id_entry.get()
        name=self.client_name_entry.get()
        address =self.client_adress_entry.get()
        contact_details=self.client_contact_details_entry.get()
        budget=self.client_budget_details_entry.get()
        if all([client_id,name,address,contact_details,budget]):
            client1(client_id,name,address,contact_details,budget).save()
            messagebox.showinfo("info","client details have all been added")
        else:
            messagebox.showerror("error","you need to fill out all the boxes")


    def modifyclinetsdetails(self): #This define function is for modifying input from the user
        client_id=self.client_id_entry.get()
        client= client1.load(client_id)
        if client:
            client.name=self.client_name_entry.get()
            client.address =self.client_adress_entry.get()
            client.contact_details=self.client_contact_details_entry.get()
            client.budget=self.client_budget_details_entry.get()
            messagebox.showinfo("info","clients details have been modifyied")
        else:
            messagebox.showerror("error","we cannot find that client")


    def deleteclinetsdetails(self): #This define function is for deleteing input from the user
        client_id = self.client_id_entry.get()
        client =client1.load(client_id)
        if client:
            client.delete()
            messagebox.showinfo("info","all client deltails have been deleted")
        else:
            messagebox.showerror("error","we cannot find that client")

    def displayclinetsdetails(self): #This define function is for displaying input from the user
        client_id = self.client_id_entry.get()
        client = client1.load(client_id)
        if client:
            info = f"ID: {client.client_id}\nClients name: {client.name}\nClients address: {client.address}\nclients contact details: {client.contact_details}\nclients budget: {client.budget}"
            messagebox.showinfo("Client Details", info)
        else:
            messagebox.showerror("error","we connot find that client")

if __name__=="__main__":
    root = tk.Tk()
    app= Clientsystem(root)
    root.mainloop()

