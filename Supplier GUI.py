import tkinter as tk
from tkinter import messagebox
import pickle
import os

class supplier :  #creating a class for the supplier
    def __init__ (self, supplier_id_, name, address, contact_details, service_provided):  #Initialiser for all The attributes pertaining to supplier
        self.supplier_id_=supplier_id_
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.service_provided=service_provided

    def save(self):
        with open(f'supplier_{self.supplier_id_}.pkl','wb')as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def load(supplier_id_):
        try:
            with open(f'supplier_{supplier_id_}.pkl', 'rb') as input:
                return pickle.load(input)
        except FileNotFoundError:
            return None

    def delet(self):
        os.remove(f'supplier_{self.supplier_id_}.pkl')

class supplierGUI:
    def __init__(self,master):
        self.master=master
        master.title("Platform for supplier management")

        tk.Label(master,text="Suppliers ID").grid(row=0)
        self.supplier_id__entry=tk.Entry(master)
        self.supplier_id__entry.grid(row=0,column=1)

        tk.Label(master, text="Suppliers name").grid(row=1)
        self.suppliername_entry = tk.Entry(master)
        self.suppliername_entry.grid(row=1, column=1)

        tk.Label(master, text="Suppliers address").grid(row=2)
        self.supplieraddress_entry = tk.Entry(master)
        self.supplieraddress_entry.grid(row=2, column=1)

        tk.Label(master, text="Suppliers contact detais").grid(row=3)
        self.suppliercontact_entry = tk.Entry(master)
        self.suppliercontact_entry.grid(row=3, column=1)

        tk.Label(master, text="Suppliers serivace provided").grid(row=4)
        self.supplierservice_entry = tk.Entry(master)
        self.supplierservice_entry.grid(row=4, column=1)

        self.add=tk.Button(master,text="add supplier details",command=self.addsuppliersdetails)
        self.add.grid(row=5,column=0)

        self.mod = tk.Button(master, text="modify supplier details", command=self.modifysuppliersdetails)
        self.mod.grid(row=5, column=1)

        self.dele = tk.Button(master, text="delete supplier details", command=self.deletesuppliersdetails)
        self.dele.grid(row=6, column=0)

        self.dis = tk.Button(master, text="display supplier details", command=self.displaysuppliersdetails)
        self.dis.grid(row=6, column=1)

    def addsuppliersdetails(self):
        supplier_id_=self.supplier_id__entry.get()
        name=self.suppliername_entry.get()
        address=self.supplieraddress_entry.get()
        contact_details=self.suppliercontact_entry.get()
        serivece_provided=self.supplierservice_entry.get()
        if all([supplier_id_,name,address,contact_details,serivece_provided]):
            supplier(supplier_id_,name,address,contact_details,serivece_provided).save()
            messagebox.showinfo("info","all suplier details have been added ")
        else:
            messagebox.showerror("error","we cannot find the supplier")

    def modifysuppliersdetails(self):
        supplier_id_ = self.supplier_id__entry.get()
        supplier1=supplier.load(supplier_id_)
        if supplier1:
            supplier1.name=self.suppliername_entry.get()
            supplier1.address=self.supplieraddress_entry.get()
            supplier1.contact=self.suppliercontact_entry.get()
            supplier1.service_provided=self.supplierservice_entry.get()
            supplier1.save()
            messagebox.showinfo("info", "all suplier details have been modified ")
        else:
            messagebox.showerror("error", "we cannot find the supplier")

    def deletesuppliersdetails(self):
        supplier_id_ = self.supplier_id__entry.get()
        supplier1 = supplier.load(supplier_id_)
        if supplier1:
            supplier1.delete()
            messagebox.showinfo("info", "all suplier details have been deleted ")
        else:
            messagebox.showerror("error", "we cannot find the supplier")


    def displaysuppliersdetails(self):
        supplier_id_ = self.supplier_id__entry.get()
        supplier1 = supplier.load(supplier_id_)
        if supplier1:
            info=f"Supplier ID{supplier1.supplier_id}\n supplier Name:{supplier1.name}\nSuppliers address:{supplier1.address}\nsuppliers contact details{supplier1.contact}\n supplier serivce provided{supplier1.service_provided}"
            messagebox.showinfo("suppliers details ",info)
        else:
            messagebox.showerror("error","we connot find the supplier")

if __name__=="__main__":
    root = tk.Tk()
    app = supplierGUI(root)
    root.mainloop()




