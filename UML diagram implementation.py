class employess : #creating a class for the employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl ): #Initialiser for all The attributes pertaining to employee
        self.name=name
        self.ID=ID
        self.department=department
        self.jod_titel=jod_titel
        self.basic_salary=basic_salary
        self.age=age
        self.DOB=DOB
        self.passportdetaisl=passportdetaisl

    def addemployeedetails (self) :
        pass
    def deletemployeedetails (self) :
        pass
    def modifyemployeedetails (self) :
        pass
    def displayemployeedetails (self) :
        pass
    def displayinformation (self) :
        pass
class handyman (employess): # Creating a class handyman which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl, tools_collected) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl ) #Initialising attributes from the parent class.
        self.tools_collected =tools_collected
    def estimate_repair_cost(self):
        pass
class designer (employess): # Creating a class designer which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,portfolio ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.portfolio=portfolio

    def update_portfolio (self):
        pass
class accountants (employess): # Creating a class accountants which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,accounts_managed ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.accounts_managed=accounts_managed

    def show_financal_statments(self):
        pass
class marketers (employess) : # Creating a class marketers which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,social_media_followers ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.social_media_followers=social_media_followers

    def createcontent(self):
        pass

class marketing_manager (employess) : # Creating a class marketing manager which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,marketing_campagin ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.marketing_campagin=marketing_campagin

    def displaycampagin(self):
        pass
class sales_person (employess) : # Creating a class sales person which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,manager_id ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.manager_id=manager_id

    def assignid (self):
        pass
class sales_manager (employess) : # Creating a class sales_manager which inherits attributes from employee
    def __init__ (self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl,regoin ) :
        super().__init__(self, name, ID, department, jod_titel, basic_salary, age, DOB, passportdetaisl)  # Initialising attributes from the parent class
        self.regoin=regoin

    def assignarea (self):
        pass

class client : #creating a class for the client
    def __init__(self,client_id,name,address,contact_details,budget): #Initialiser for all The attributes pertaining to client
        self.client_id=client_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.budget=budget

    def addclientdetails (self):
        pass
    def deletclientdetails (self):
        pass
    def modifyclientdetails (self):
        pass
    def displayclientdetails(self):
        pass
    def displayinformation1 (self):
        pass

class supplier :  #creating a class for the supplier
    def __init__ (self, supplier_id, name, address, contact_details, service_provided):  #Initialiser for all The attributes pertaining to supplier
        self.supplier_id=supplier_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.service_provided=service_provided

    def addsupplierdetails (self):
        pass
    def deletsuppleirdetails(self):
        pass
    def modifysupplierdetails(self):
        pass
    def deletsupplierdetails (self):
        pass
    def displayinformation (self):
        pass
class event :  #creating a class for the event
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
    def addeventdetails (self):
        pass
    def deleteventdetails(self):
        pass
    def modifyeventdetails(self):
        pass
    def deleteventdetails (self):
        pass
    def displayinformation (self):
        pass

class graduation (event): # Creating a class graduation which inherits attributes from event
    def __init__(self,event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice,school_name):# Initialising attributes from the parent class
        super().__init__(event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice)
        self.school_name=school_name

    def provide_diploma(self):
        pass

class themed_party (event): # Creating a class themed part which inherits attributes from event
    def __init__(self,event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice,theme_type):# Initialising attributes from the parent class
        super().__init__(event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice)
        self.theme_type=theme_type

    def decorate_theme(self):
        pass

class birthday (event): # Creating a class birthday which inherits attributes from event
    def __init__(self,event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice, birthday_person):# Initialising attributes from the parent class
        super().__init__(event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice)
        self.birthday_person=birthday_person

    def provid_cake(self):
        pass
class wedding (event): # Creating a class wedding which inherits attributes from event
    def __init__(self,event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice, couple_name):# Initialising attributes from the parent class
        super().__init__(event_id, type, theme, date, time, duration, venue, client,guest_list,catering_company,deco_company, entert_company, furnitur_supplier, invoice)
        self.couple_name=couple_name

    def displayname(self):
        pass

class guest :#creating class guest
    def __init__(self,guest_id, name, address, contact_details): #Initialiser for all The attributes pertaining to guest
        self.guest_id=guest_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
    def addguestdetails (self) :
        pass
    def deletguestdetails (self) :
        pass
    def modifyguestdetails (self) :
        pass
    def displayguestdetails (self) :
        pass
    def displayinformation (self) :
        pass

class venue : #creating a class venue
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guest): #Initialiser for all The attributes pertaining to venue
        self.venue_id=venue_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.min_guests=min_guests
        self.max_guest=max_guest

    def displayinformation(self):
        pass

class caterer :  #creating a class caterer
    def __init__(self,caterer_id, name, address, contact_details, menu, min_guest, max_guest): #Initialiser for all The attributes pertaining to caterer
        self.caterer_id=caterer_id
        self.name=name
        self.address=address
        self.contact_details=contact_details
        self.menu=menu
        self.min_guest=min_guest
        self.max_guest=max_guest
    def displayinformation(self):
        pass