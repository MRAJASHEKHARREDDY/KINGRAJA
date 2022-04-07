#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Theater:
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.booking_details = {}
        
    def show_seats(self):
        for row in range(self.rows+1):
            for col in range(self.columns+1):
                if row==0:
                    if col==0:
                        print(" ", end=" ")
                    else:
                        print(col, end=" ")
                else:
                    if col==0:
                        print(row, end=" ")
                    else:
                        seat_id = str(row)+str(col)
                        if seat_id in self.booking_details:
                            print("B", end=" ")
                        else:
                            print("S", end=" ")
            print()
    def buy_ticekt(self):
        row = int(input("Please enter the row in which you want to book the seat: "))
        col = int(input("Please enter the seat number in the row which you want to book: "))
        #rules for price
        seat_id = str(row)+str(col)
        if seat_id in self.booking_details:
            print("Ticket is book already!!!")
            return 
        total_seats = self.rows * self.columns
        if total_seats<=60:
            price = 10
        else:
            half_factor=self.rows//2
            if row <= half_factor:
                price = 10
            else:
                price = 8

        should_book = int(input(f"Here is the price for seat number {col} in row {row}: {price}\nDo you want to book the seat?\n1. Yes\n2. No\n Please your choice: "))
        
        if should_book == 1:
            name = input("Please enter your name: ")
            age = input("Please enter your age: ")
            gender = input("Please enter your gender: ")
            number = input("Please enter your mobile number: ")
            # save this details somewhere
            
            details = {}
            details['name']=name
            details['age']=age
            details['gender']=gender
            details['number']=number
            details['price']=price
            self.booking_details[seat_id]=details
            print("Ticket Booked succesfully")
        else:
            print("You decided not to book the seat.")
            
    def show_statics(self):
        purchased_tickets = len(self.booking_details)
        total_seats = self.rows*self.columns
        
        percentage_of_ticket_booked = (purchased_tickets/total_seats)*100
        
        current_income=0
        for seat_id in self.booking_details:
            details = self.booking_details[seat_id]
            current_income+=details['price']
        
        #total income
        total_income = 0
        total_seats = self.rows * self.columns
        if total_seats<=60:
            price = 10
            total_income = total_seats*price
        else:
            # rows = 9 columns = 8
            half_factor=self.rows//2 # half_factore = 4
            
            first_half_row_price = 10
            first_half_row_seats = half_factor*self.columns # 4*8 =32
            first_half_row_total_price = first_half_row_seats*first_half_row_price # 32*10=320
            
            second_half_row_price = 8
            second_half_row_seats = (self.rows-half_factor)*self.columns # 5*8 = 40
            second_half_row_total_price = second_half_row_seats*second_half_row_price # 40*8=320
            total_income = first_half_row_total_price + second_half_row_total_price #640
                
        print("Number of Purchased Tickets: ",purchased_tickets)
        print("Percentage of Tickets booked: ",round(percentage_of_ticket_booked,2))
        print("Current Income: ",current_income)
        print("Total Income: ",total_income)

        
    def show_user_details(self):
        row = int(input("Please enter the row for which you want to see the booking details: "))
        col = int(input("Please enter the seat number in the row for which you want to see the booking details: "))
        seat_id = str(row)+str(col)
        if seat_id in self.booking_details:
            details = self.booking_details[seat_id] #{'name':"dipesh"}
            print(f"Here is the details of user who has booked seat {col} in row {row}: ")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Gender: {details['gender']}")
            print(f"Number: {details['number']}")
            print(f"Book for price: {details['price']} $")
        else:
            print("Seat is not booked so can't show the details")
    

rows = int(input("Please enter number of rows: "))
columns = int(input("Please enter number of seats in each rows: "))

theater = Theater(rows,columns)

while True:
    choice = int(input("1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked Tickets User Info\n0. Exit\nEnter your choice here: "))
    if choice == 1:
        theater.show_seats()
    elif choice == 2:
        theater.buy_ticekt()
    elif choice == 3:
        theater.show_statics()
    elif choice == 4:
        theater.show_user_details()
    elif choice == 0:
        print("Okay bye!!! See YOU Soon!!! Thank You!!!")
        break
    else:
        print("Invalid choice please choose a option from below: ")
    


# In[ ]:





# In[ ]:




