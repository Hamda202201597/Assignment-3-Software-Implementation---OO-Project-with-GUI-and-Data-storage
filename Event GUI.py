import tkinter as tk
from tkinter import messagebox, Entry, Label, Button, Frame
import pickle
import os

class Event:
    def __init__(self,event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice): #Initialiser is for the event attributes
        self.event_id=event_id
        self.type=type
        self.theme=theme
        self.date=date
        self.time=time
        self.duration=duration
        self.venue=venue
        self.client=client
        self.guest_list=guest_list
        self.catering_company=catering_company
        self.deco_company=deco_company
        self.entert_company=entert_company
        self.furnitur_supplier=furnitur_supplier
        self.invoice=invoice

    def show_all_information(self):
        return(f"Events ID: {self.event_id}, Type of Event: {self.type}, Event's theme{self.theme}, Date of event: {self.date}"
               f"Time of the event: {self.time}, The duration of the event{self.duration}, venue event is taking place in:{self.venue},"
               f"Clients:{self.client},Guests of the event{len(self.guest_list)}, Catering for the event:{self.catering_company},"
               f"Decoration compnay :{self.deco_company}, entertaimnet company:{self.entert_company},furniture supplier:{self.furnitur_supplier}, invoice for the event:{self.invoice}")
events={}
root=tk.Tk()
root.title("platform for manganing events")
frame=Frame(root)
frame.pack(pady=40,padx=40)

entries={}
fields=['Events ID','Type of Event','Events theme','Date of event','Time of the event','The duration of the event','venue event is taking place in','Clients','Guests of the event',' Catering for the event','Decoration compnay','entertaimnet company','furniture supplier','invoice for the event']

for field in fields:
    row = Frame(frame)
    label = Label(row, width=44, text=field + ": ", anchor='w')
    entry = Entry(row)
    row.pack(side='top', fill='x', padx=5, pady=5)
    label.pack(side='left')
    entry.pack(side='right', expand=True, fill='x')
    entries[field] = entry

def add_event_details():
    try:
        event_id=entries['Events ID'].get()
        if event_id in events:
            messagebox.showerror("error","events id is already in use")
            return
        event_data={field: entries[field].get()for field in fields if field != 'event id'}
        event_data['guest_list']=event_data['Guest List'].split(',')
        event = Event(event_id, **event_data)
        events[event_id] = event
        messagebox.showinfo("sucess"," the event has been sucseessfully added")
    except Exception as e :
        messagebox.showerror("error",str(e))

def show_event_information ():
    event_id = entries['event ID'].get()
    event=events.get(event_id)
    if event_id in events:
        messagebox.showinfo("events details",event.show_event_information())
    else:
        messagebox.showerror("error","that event doesnt exsist")

def delete_event():
    event_id = entries['event ID'].get()
    if event_id in events:
        del events[event_id]
        messagebox.showinfo("sucess", "the event was sucessfully deleted")
    else:
        messagebox.showerror("error", "that event doesnt exsist")

Button(frame,text="add the event",command=add_event_details).pack(side='left',padx=5)
Button(frame,text="display all the events",command=show_event_information).pack(side='left',padx=5)
Button(frame,text="delet event", command=delete_event).pack(side='left',padx=5)

root.mainloop()

def saveevens(events):
    with open("eventsgui.dat","wb") as file:
        pickle.dumo(events,file)

def loadevents():
    if os.path.exists("eventsgui.dat"):
        with open ("eventsgui.dat","rb") as file:
            return pickle.load(file)
    else:
        return{}

events = loadevents()