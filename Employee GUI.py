import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os

class employess:  # Creating a class for the employee
    def __init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl, manager_id):
        self.name = name
        self.ID = ID
        self.department = department
        self.jod_titel = jod_titel
        self.basic_salary = basic_salary
        self.age = age
        self.DOB = DOB
        self.passportdetaisl = passportdetaisl
        self.manager_id = manager_id
    def save(self):  #saving the class to a file
        with open(f'employee_{self.ID}.pkl','wb') as output:
            pickle.dump(self,output,pickle.HIGHEST_PROTOCOL)

    def load(ID):  # loading and returning object from the file
        try:
            with open(f'employee_{ID}.pkl','rb') as input:
                return pickle.load(input)
        except FileNotFoundError:
            return None

    def delete(self): #deleteing the file that has the pickle
        os.remove(f'employee_{self.ID}.pkl')

class emoplyeeGUI: #starting the gui for emplyee manmgemnt
    def __init__(self,master):
        self.master = master
        master.title("Platform for employee management")

        # adding all the lables and boxes for the client attributes
        tk.Label(master,text="emplyee ID:").grid(row=0)
        self.emplyeeid_entry=tk.Entry(master)
        self.emplyeeid_entry.grid(row=0,column=1)

        tk.Label(master, text="emplyee Name:").grid(row=1)
        self.emplyeename_entry = tk.Entry(master)
        self.emplyeename_entry.grid(row=1, column=1)

        tk.Label(master, text="emplyees department:").grid(row=2)
        self.emplyeedepartment_entry = tk.Entry(master)
        self.emplyeedepartment_entry.grid(row=2, column=1)

        tk.Label(master, text="emplyees job title:").grid(row=3)
        self.emplyeejobtitle_entry = tk.Entry(master)
        self.emplyeejobtitle_entry.grid(row=3, column=1)

        tk.Label(master, text="emplyees basic salary:").grid(row=4)
        self.emplyeebasicsalary_entry = tk.Entry(master)
        self.emplyeebasicsalary_entry.grid(row=4, column=1)

        tk.Label(master, text="emplyees age:").grid(row=5)
        self.emplyeeage_entry = tk.Entry(master)
        self.emplyeeage_entry.grid(row=5, column=1)

        tk.Label(master, text="emplyees date of birth:").grid(row=6)
        self.emplyeedateofbirth_entry = tk.Entry(master)
        self.emplyeedateofbirth_entry.grid(row=6, column=1)

        tk.Label(master, text="emplyees passport details:").grid(row=7)
        self.emplyeepassportdetails_entry = tk.Entry(master)
        self.emplyeepassportdetails_entry.grid(row=7, column=1)

        tk.Label(master, text="emplyees manager ID:").grid(row=8)
        self.emplyeemanagerid_entry = tk.Entry(master)
        self.emplyeemanagerid_entry.grid(row=8, column=1)

        # adding the buttons

        self.add=tk.Button(master,text="add employee details",command=self.addemployeedetails)
        self.add.grid(row=9,column=0)

        self.mod = tk.Button(master, text="modify employee details", command=self.modiefyemployeedetails)
        self.mod.grid(row=9, column=1)

        self.delete = tk.Button(master, text="delete employee details", command=self.deleteemployeedetails)
        self.delete.grid(row=10, column=0)

        self.display = tk.Button(master, text="display employee details", command=self.displayemployeedetails)
        self.display.grid(row=10, column=1)

    def addemployeedetails(self): #This define function is for colleting input from the user and savinf it all
        employees_id =self.emplyeeid_entry.get()
        name=self.emplyeename_entry.get()
        department=self.emplyeedepartment_entry.get()
        job_title=self.emplyeejobtitle_entry.get()
        basic_salary=self.emplyeebasicsalary_entry.get()
        age=self.emplyeeage_entry.get()
        bateofbirth=self.emplyeedateofbirth_entry.get()
        passportdetails=self.emplyeepassportdetails_entry.get()
        managerid=self.emplyeemanagerid_entry.get()
        if all([employees_id,name,department,job_title,basic_salary,age,bateofbirth,passportdetails,managerid]):
            employess(name,employees_id,department,job_title,basic_salary,age,bateofbirth,passportdetails,managerid).save()
            messagebox.showinfo("info","all employee details have been added")
        else:
            messagebox.showerror("error","answer all the boxes")

    def modiefyemployeedetails(self): #This define function is for modifying input from the user
        employees_id = self.emplyeeid_entry.get()
        employee=employess.load(employees_id)
        if employee:
            employee.name=self.emplyeename_entry.get()
            employee.department=self.emplyeedepartment_entry.get()
            employee.job_title=self.emplyeejobtitle_entry.get()
            employee.basic_salary=self.emplyeebasicsalary_entry.get()
            employee.age=self.emplyeeage_entry.get()
            employee.bateofbirth=self.emplyeedateofbirth_entry.get()
            employee.passportdetails=self.emplyeepassportdetails_entry.get()
            employee.managerid=self.emplyeemanagerid_entry.get()
            employee.save()
            messagebox.showinfo("info", "all employee details have been modified")
        else:
            messagebox.showerror("error", "we cannot find employee")

    def deleteemployeedetails(self): #This define function is for deleteing input from the user
        employees_id = self.emplyeeid_entry.get()
        employee = employess.load(employees_id)
        if employee:
            employee.delete()
            messagebox.showinfo("info", "all employee details have been deleted")
        else:
            messagebox.showerror("error", "we cannot find employee")

    def displayemployeedetails(self): #This define function is for displaying input from the user
        employees_id = self.emplyeeid_entry.get()
        employee = employess.load(employees_id)
        if employee:
            info=f"employee ID:{employee.ID}\nemployee Name:{employee.name}\nemployee department: {employee.department}\nemployee job title: {employee.job_title}\nemployee basic salary: {employee.basic_salary}\nemployee age: {employee.age}\nemlpoyee date of birth: {employee.DOB}\nemployee passport details: {employee.passport_details}\nemployee manager ID: {employee.manager_id}"
            messagebox.showinfo("all employee details have been displayed",info)
        else:
            messagebox.showerror("error", "we cannot find employee")

if __name__=="__main__":
    root=tk.Tk()
    app=emoplyeeGUI(root)
    root.mainloop()



