import subprocess as sp
import pymysql
import pymysql.cursors
import datetime


def insertCustomer(): #INSERT Query
    try:
        # Takes luggage details as input
        row = {}
        print("Enter new customer's details: ")
        row["Fname"] = input("Customer's First Name: ")
        row["Mname"] = input("Customer's Middle Name: ")
        row["Lname"] = input("Customer's Last Name: ")
        row["Phone_no"] = input("Phone Number: ")
        row["Business_provided_till_now"] = int(input("Business provided till now: "))
        row["Birthday"] = input("Birthday in (YYYY-MM-DD)format: ")
        row["Table_Number"] = int(input("Table No: "))
        # date_time=row['Birthday'].strftime('%Y-%m-%d')
        # print(row["Birthday"])
        query_init0="SELECT TABLE_INFO.Status as st FROM TABLE_INFO WHERE TABLE_INFO.Table_Number='%d'" %(row["Table_Number"])
        cur.execute(query_init0)
        con.commit()
        output = cur.fetchall()
        for x in output:
            if x["st"]=="Occupied":
                print("The given table number is already occupied")
                return
        query = "INSERT INTO CUSTOMER(Fname, Mname, Lname, Phone_No, Business_provided_till_now, Birthday, Table_Number) VALUES('%s', '%s', '%s', '%s', '%d', '%s', '%d')" % (
            row["Fname"], row["Mname"], row["Lname"], row["Phone_no"], row["Business_provided_till_now"], row["Birthday"], row["Table_Number"])

        print(query)
        cur.execute(query)
        con.commit()
        query5 = "UPDATE TABLE_INFO SET Status='Occupied' WHERE Table_Number='%d'"%(row["Table_Number"])
        cur.execute(query5)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def AssignMentor(): #UPDATE Query
    try:
        row = {}
        row["Waiter_ID"] = input("Enter Waiter ID of waiter being metored: ")
        row["Mentor_ID"] = input("Enter Waiter ID of mentee waiter: ")
        query0="SELECT Waiter_ID FROM WAITER WHERE Waiter_ID='"+row["Waiter_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The waiter with waiter id {row['Waiter_ID']} doesn't exist in database")
            return
        query = "UPDATE WAITER SET Mentor_ID='%s' WHERE Waiter_ID='%s'" % (
            row["Mentor_ID"], row["Waiter_ID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def ChangeWaiterSalary(): #UPDATE Query
    try:
        row = {}
        row["Waiter_ID"] = input("Enter Waiter ID of waiter: ")
        row["Salary"] = int(input("Enter new salary: "))

        query0 = "SELECT Waiter_ID FROM WAITER WHERE Waiter_ID='"+row["Waiter_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The waiter with waiter id {row['Waiter_ID']} doesn't exist in database")
            return
         
        query = "UPDATE WAITER SET Salary='%d' WHERE Waiter_ID='%s'" % (
            row["Salary"], row["Waiter_ID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")
    
    except Exception as e:  
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    
    return

def ChangeChefSalary(): #UPDATE Query
    try:
        row = {}
        row["Chef_ID"] = input("Enter Chef ID of chef: ")
        row["Salary"] = int(input("Enter new salary: "))

        query0 = "SELECT Chef_ID FROM CHEF WHERE Chef_ID='"+row["Chef_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The chef with chef id {row['Chef_ID']} doesn't exist in database")
            return

        query = "UPDATE CHEF SET Salary='%d' WHERE Chef_ID='%s'" % (
            row["Salary"], row["Chef_ID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)
    
    return

def insertTable():  # INSERT Query
    try:
        # Takes ticket details as input
        row = {}
        print("Enter new table's details: ")
        row["Table_Num"] = int(input("Table Number: "))
        row["Section_Type"] = input("Section Type (Private Room or Dining or Terrace): ")
        row["Seating_Capacity"] = int(
            input("Seating Capacity: "))
        row["Status"] = input("Status (Occupied or Not occupied): ")

        query = "INSERT INTO TABLE_INFO(Table_Number, Section_Type, Seating_Capacity, Status) VALUES('%d', '%s', '%d', '%s')" % (
            row["Table_Num"], row["Section_Type"], row["Seating_Capacity"], row["Status"])
        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertCombo():  # INSERT Query
    try:
        # Takes luggage details as input
        row = {}
        print("Enter new combo's details: ")
        row["Name"] = input("Combo's Name: ")
        row["Price"] = int(input("Combo's Price: "))
        row["Availability"] = bool(input("Combo's Availability: "))
        # row["Type"]=input("Give Combo's Type:")
        num=int(input("Give no. of dishes combo contains:"))
        num2=int(input("Give number of combo's types(Lunch Combo or Dinner Combo or Weekend Special):"))
        lst2=[]
        lst=[]
        for x in range(num):
            dish_name=input("give dish name:")
            query10="SELECT Name FROM DISH WHERE Name='"+dish_name+"'"
            cur.execute(query10)
            con.commit()
            output1 = cur.fetchall()
            # print(output1)
            for y in output1:
                if y['Name']==dish_name:
                    lst.append(dish_name)
                else:
                    print(f"The dish named {dish_name} doesn't exist in table")
                    return
            if len(output1)==0:
                print(f"The dish named {dish_name} doesn't exist in table")
                return
            
        for x in range(num2):
            type_name=input("give dish type:")
            query20="SELECT DISTINCT Type FROM COMBO_TYPE WHERE Type='"+type_name+"'"
            cur.execute(query20)
            con.commit()
            output2 = cur.fetchall()
            # print(output2)
            for y in output2:
                if y['Type']==type_name:
                    lst2.append(type_name)
                else:
                    print(f"The type named {type_name} doesn't exist in table")
                    return
            if len(output2)==0:
                print(f"The type named {type_name} doesn't exist in table")
                return
        
        for x in range(num):
            query11="INSERT INTO COMBO(Name,Dish_name,Price,Availability) VALUES('%s','%s','%d','%d')" %(row["Name"],lst[x],row["Price"],row["Availability"])
            cur.execute(query11)
            con.commit()
        for y in range(num2):
            for x in range(num):
                query12="INSERT INTO COMBO_TYPE(Name,Dish_name,Type) VALUES('%s','%s','%s')" %(row["Name"],lst[x],lst2[y])
                cur.execute(query12)
                con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertChef():   # INSERT Query
    try:
        # Takes driver details as input
        row = {}
        print("Enter new Chef: ")
        row["chef_id"] = input("Chef ID: ")
        row["First_Name"] = input("First Name: ")
        row["Middle_Name"] = input("Middle Name: ")
        row["Last_Name"] = input("Last Name: ")
        row["Date_of_join"] = input("Date of join: ")
        row["Rating"] = int(input("Rating: "))
        row["Salary"] = int(input("Salary: "))
        row["St_shift"]=input("Give shift start time (HH:MM:SS):")
        row["end_shift"]=input("Give shift end time (HH:MM:SS):")
        num=int(input("Give no. of dishes in which chef is specialised:"))
        lst=[]
        for x in range(num):
            dish_name=input("give dish name:")
            query10="SELECT Name FROM DISH WHERE Name='"+dish_name+"'"
            cur.execute(query10)
            con.commit()
            output1 = cur.fetchall()
            print(output1)
            for y in output1:
                if y['Name']==dish_name:
                    lst.append(dish_name)
                else:
                    print(f"The dish named {dish_name} doesn't exist in table")
                    return
            if len(output1)==0:
                print(f"The dish named {dish_name} doesn't exist in table")
                return
        query2 = "INSERT INTO CHEF(Chef_ID, Fname, Mname, Lname,Date_of_join,Rating,Salary) VALUES('%s', '%s', '%s', '%s','%s','%d','%d')" % (
            row["chef_id"], row["First_Name"], row["Middle_Name"], row["Last_Name"],row["Date_of_join"],row["Rating"],row["Salary"])

        print(query2)
        cur.execute(query2)
        con.commit()
        for x in range(num):
            query11="INSERT INTO CHEF_SPECIALISATION(Chef_ID,Dish_name) VALUES('%s','%s')" %(row["chef_id"],lst[x])
            cur.execute(query11)
            con.commit()

        query1="INSERT INTO CHEF_SHIFT(Chef_ID,Shift_Start_time,Shift_end_time) VALUES('%s','%s','%s')" %(row["chef_id"],row["St_shift"],row["end_shift"])
        cur.execute(query1)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertWaiter(): # INSERT Query
    try:
        # Takes driver details as input
        row = {}
        print("Enter new Waiter: ")
        row["Waiter_ID"] = input("Waiter ID: ")
        row["First_Name"] = input("First Name: ")
        row["Middle_Name"] = input("Middle Name: ")
        row["Last_Name"] = input("Last Name: ")
        row["Date_of_join"] = input("Date of join: ")
        row["Rating"] = int(input("Rating: "))
        row["Salary"] = int(input("Salary: "))
        row["Number_of_tables_served_this_month"]=int(input("No. of tables served this month:"))
        row["Mentor_ID"]=input("Mentor ID:")
        row["St_shift"]=input("Give shift start time (HH:MM:SS):")
        row["end_shift"]=input("Give shift end time (HH:MM:SS):")
        
        null_string=""
        if row["Mentor_ID"]=="NULL":
            query2 = "INSERT INTO WAITER(Fname, Mname, Lname, Waiter_ID,Date_of_join,Rating,Number_of_tables_served_this_month,Salary) VALUES('%s','%s','%s','%s','%s','%d','%d','%d')" % (
                row["First_Name"], row["Middle_Name"], row["Last_Name"],row["Waiter_ID"],row["Date_of_join"],row["Rating"],row["Number_of_tables_served_this_month"],row["Salary"])
        else:
            query2 = "INSERT INTO WAITER(Fname, Mname, Lname, Waiter_ID,Date_of_join,Rating,Number_of_tables_served_this_month,Salary,Mentor_ID) VALUES('%s','%s','%s','%s','%s','%d','%d','%d','%s')" % (
                row["First_Name"], row["Middle_Name"], row["Last_Name"],row["Waiter_ID"],row["Date_of_join"],row["Rating"],row["Number_of_tables_served_this_month"],row["Salary"],row["Mentor_ID"])


        print(query2)
        cur.execute(query2)
        con.commit()

        query1="INSERT INTO WAITER_SHIFT(Waiter_ID,Shift_Start_time,Shift_end_time) VALUES('%s','%s','%s')" %(row["Waiter_ID"],row["St_shift"],row["end_shift"])
        cur.execute(query1)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertSupplier():   # INSERT Query
    try:
        # Takes driver details as input
        row = {}
        print("Enter new Supplier: ")
        row["Supplier_ID"] = input("Supplier ID: ")
        row["First_Name"] = input("First Name: ")
        row["Middle_Name"] = input("Middle Name: ")
        row["Last_Name"] = input("Last Name: ")
        row["House_No"] = input("House No: ")
        row["Street"] = input("Street: ")
        row["pincode"] = int(input("Pincode: "))
        row["Phone_num"]=input("Phone_No:")
        row["Transaction Amount"]=int(input("Transaction Amount:"))

        

   
        query2 = "INSERT INTO SUPPLIER(Supplier_ID,Fname, Mname, Lname,House_No,Street,Pincode,Phone_No,Transaction_Amount) VALUES('%s','%s','%s','%s','%s','%s','%d','%s','%d')" % (
             row["Supplier_ID"], row["First_Name"], row["Middle_Name"],row["Last_Name"],row["House_No"],row["Street"],row["pincode"],row["Phone_num"],row["Transaction Amount"])


        print(query2)
        cur.execute(query2)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertDish():   # INSERT Query
    try:
        # Takes driver details as input
        row = {}
        print("Enter new Dish: ")
        row["Name"] = input("Name: ")
        row["Category"] = input("Category (Veg or Non-veg or Vegan): ")
        row["Cuisine"] = input("Cuisine (Indian or Italian or Chinese): ")
        row["Description"] = input("Description: ")
        row["Price"] = int(input("Price: "))
        num=int(input("Give no. of ingredients dish needs:"))
        lst=[]
        for x in range(num):
            ig_name=input("give ingredient name:")
            query10="SELECT Name FROM INGREDIENT WHERE Name='"+ig_name+"'"
            cur.execute(query10)
            con.commit()
            output1 = cur.fetchall()
            # print(output1)
            for y in output1:
                if y['Name']==ig_name:
                    lst.append(ig_name)
                else:
                    print(f"The ingredient named {ig_name} doesn't exist in table")
                    return
            if len(output1)==0:
                print(f"The ingredient named {ig_name} doesn't exist in table")
                return
            
   
        query2 = "INSERT INTO DISH(Name,Category, Cuisine, Description,Price) VALUES('%s','%s','%s','%s','%d')" % (
             row["Name"], row["Category"], row["Cuisine"],row["Description"],row["Price"])


        print(query2)
        cur.execute(query2)
        con.commit()
        
        for x in range(num):
            query11="INSERT INTO DISH_REQUIREMENT(Dish_Name,Ingredient) VALUES('%s','%s')" %(row["Name"],lst[x])
            cur.execute(query11)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def allOrdersOfaCustomers():
    try:
        phone_num=input("Give phone number of customer:")
        query="SELECT * FROM ORDER_INFO WHERE Customer_Phone_No='"+phone_num+"'"
        print(query)
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"\nOrder_num :{x['Order_Number']}  Date:{x['Date']}  Time:{x['Time']}  Total Price:{x['Total_price']}  Phone No:{x['Customer_Phone_No']}  Rating:{x['Rating']}  Comment:{x['Comment']}  Dishes :",end='')
            query2="SELECT Dish_name FROM (ORDER_INFO INNER JOIN ORDER_DISHES ON ORDER_INFO.Order_Number=ORDER_DISHES.Order_Number) WHERE ORDER_INFO.Order_Number='"+str(x["Order_Number"])+"'"
            cur.execute(query2)
            con.commit()
            output2 = cur.fetchall()
            for y in output2:
                print(f"{y['Dish_name']}   ",end='')
                # print(y)
            print("\n")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def allDishesOfCategory():
    try:
        category=input("Give category of dishes you want to search(Vegan or Veg or Non-veg):")
        query="SELECT Name,Category,Cuisine,Description,Price FROM DISH WHERE Category='"+category+"'"
        cur.execute(query)
        con.commit()
        output=cur.fetchall()
        for x in output:
            print(f"\nName:{x['Name']}  Category:{x['Category']}  Cuisine:{x['Cuisine']}  Description:{x['Description']}  Price:{x['Price']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def getTotalSalaryOfChefs():
    try:
        query="SELECT SUM(Salary) AS TOTAL FROM CHEF"
        cur.execute(query)
        con.commit()
        output=cur.fetchall()
        for x in output:
            print(f"\nTotal salary sum: {x['TOTAL']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return


def highestSaleDish():
    try:
        date_from=input("Give lower bound date:")
        date_till=input("Give upper bound date:")
        query="SELECT ORDER_DISHES.Dish_Name,COUNT(*) FROM ORDER_DISHES WHERE ORDER_DISHES.Date > '" +date_from +"' AND ORDER_DISHES.Date < '"+date_till+ "' GROUP BY Dish_Name ORDER BY COUNT(*) DESC LIMIT 1"
        print(query)
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"Dish name: {x['Dish_Name']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    

    return

def maxTotalPrice():
    try:
        query="SELECT MAX(Total_price) AS MAXIMUM FROM ORDER_INFO"
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"\nMax total price of an order: {x['MAXIMUM']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    

    return

def getDishByKeyword():
    try:
        key_word=input("Give your keyword:")
        key_word=key_word.lower()
        query="SELECT Name, Description FROM DISH WHERE LOCATE('"+key_word+"', DISH.Description)!=0"
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"\nName: {x['Name']}  Description:{x['Description']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def getCustomerByLastName():   # SELECT Query
    try:    
        last_name=input("Give Last name you want to search for:")
        query="SELECT Fname, Mname, Lname, Phone_No FROM CUSTOMER WHERE Lname='"+last_name+"'"
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"\nName: {x['Fname']} {x['Mname']} {x['Lname']}    Phone Number:{x['Phone_No']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def giveTop5dishes_ac_to_feedback():
    try:
        query="SELECT Dish_name, AVG(Rating) AS AVERAGE_RATING FROM (ORDER_INFO INNER JOIN ORDER_DISHES ON ORDER_INFO.Order_Number=ORDER_DISHES.Order_Number) GROUP BY Dish_name ORDER BY AVERAGE_RATING DESC LIMIT 5"
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"\nDish Name :{x['Dish_name']}  Average Rating: {x['AVERAGE_RATING']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def bestWaiterOftheMonth():  # SELECT Query
    try:
        query="SELECT A.Fname,A.Mname,A.Lname,A.Waiter_ID,A.Mentor_ID,A.Number_of_tables_served_this_month, A.Rating*A.Number_of_tables_served_this_month as FACTOR FROM WAITER AS A ORDER BY FACTOR DESC LIMIT 1"
        cur.execute(query)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(f"NAME: {x['Fname']} {x['Mname']} {x['Lname']}  Waiter ID: {x['Waiter_ID']}  Tables served this month: {x['Number_of_tables_served_this_month']}  Factor: {x['FACTOR']}")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)


    return
def giveTotalRevenue_month():   # SELECT Query
    try:
        month=input("Give month number (01 for January to 12 for December):")
        flag=input("Give 0 to find for all years or give 1 to find for specific year:")
        if flag=='1':
            year=input("Give year (YYYY):")
            date=year+"-"+month+"-__"
            query="SELECT SUM(Total_price) AS TOTAL_REV FROM ORDER_INFO WHERE Date LIKE '"+date+"'"
            # print(query)
            cur.execute(query)
            con.commit()
            output = cur.fetchall()
            for x in output:
                print(f" Total Revenue: {x['TOTAL_REV']}")
        elif flag=='0':
            date="____-"+month+"-__"
            query="SELECT SUM(Total_price) AS TOTAL_REV FROM ORDER_INFO WHERE Date LIKE '"+date+"'"
            # print(query)
            cur.execute(query)
            con.commit()
            output = cur.fetchall()
            for x in output:
                print(f" Total Revenue: {x['TOTAL_REV']}")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return
    


    

def insertIngredients():    # INSERT Query
    try:
        # Takes driver details as input
        row = {}
        print("Enter new ingredient: ")
        row["Name"] = input("Name: ")
        row["Quantity_in_hand"] = int(input("Quantity_in_hand: "))
        row["Supplier_ID"] = input("Supplier_ID: ")


   
        query2 = "INSERT INTO INGREDIENT(Name,Quantity_in_hand, Supplier_ID) VALUES('%s','%d','%s')" % (
             row["Name"], row["Quantity_in_hand"], row["Supplier_ID"])


        print(query2)
        cur.execute(query2)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateTableStatus():    # UPDATE Query
    try:
        # Takes updated MOT preference details as input
        row = {}
        row["Table_num"] = int(
            input("Enter the Table number: "))
        row["new"] = input(
            "Enter new status for table(Occupied or Not occupied): ")
        query0="SELECT Table_Number FROM TABLE_INFO WHERE TABLE_INFO.Table_Number='"+str(row["Table_num"])+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The table with table no {row['Table_num']} doesn't exist in database")
            return
        
        query = "UPDATE TABLE_INFO SET Status='%s' WHERE Table_Number='%d'" % (
            row["new"], row["Table_num"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def insertNewOrder():   # INSERT Query
    try:
        row={}
        row["Dt"]=input("Give date:")
        row["Tm"]=input("Give time:")
        row["Tp"]=int(input("Give Total Price:"))
        row["pn"]=input("Give customer's phone number:")
        row["rt"]=int(input("Give rating:"))
        row["cmt"]=input("Give comment:")
        num=int(input("Give no. of dishes in order:"))
        lst=[]
        for x in range(num):
            dish_name=input("give dish name:")
            query10="SELECT Name FROM DISH WHERE Name='"+dish_name+"'"
            cur.execute(query10)
            con.commit()
            output1 = cur.fetchall()
            # print(output1)
            for y in output1:
                if y['Name']==dish_name:
                    lst.append(dish_name)
                else:
                    print(f"The dish named {dish_name} doesn't exist in table")
                    return
            if len(output1)==0:
                print(f"The dish named {dish_name} doesn't exist in table")
                return
            
        query0="SELECT MAX(Order_Number) AS MAXIMUM FROM ORDER_INFO WHERE Customer_Phone_No='"+row["pn"]+"' AND Date='"+row["Dt"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        for x in output0:
            if x['MAXIMUM']==None:
                row["on"]=1
            else:
                row["on"]=x["MAXIMUM"]+1
        query1="INSERT INTO ORDER_INFO(Order_Number,Date,Time,Total_price,Customer_Phone_No,Rating,Comment) VALUES('%d','%s','%s','%d','%s','%d','%s')" %(row["on"],row["Dt"],row["Tm"],row["Tp"],row["pn"],row["rt"],row["cmt"])
        cur.execute(query1)
        con.commit()
        for x in range(num):
            query11="INSERT INTO ORDER_DISHES(Order_Number,Date,Customer_Phone_No,Dish_name) VALUES('%d','%s','%s','%s')" %(row["on"],row["Dt"],row["pn"],lst[x])
            cur.execute(query11)
            con.commit()
        print("Customer's order added")
    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return

def updateCustomer_Table_BusinessProvided():    # UPDATE Query
    try:
        row = {}
        row["Table_num"]=int(input("Give new table number:"))
        row["Business_provided"]=int(input("Give new business amount:"))
        row["Phone_num"] = input("Enter Phone number of customer: ")
        query_init0="SELECT TABLE_INFO.Status as st FROM TABLE_INFO WHERE TABLE_INFO.Table_Number='%d'" %(row["Table_num"])
        cur.execute(query_init0)
        con.commit()
        output = cur.fetchall()
        for x in output:
            if x["st"]=="Occupied":
                print("The given table number is already occupied")
                return

        query_init="SELECT CUSTOMER.Business_provided_till_now FROM CUSTOMER WHERE CUSTOMER.Phone_No='%s'" %(row["Phone_num"])
        cur.execute(query_init)
        con.commit()
        output = cur.fetchall()
        for x in output:
            print(x)

        row["Business_provided"] = int(output[0]['Business_provided_till_now']+row["Business_provided"])
        print(row["Business_provided"])
        
        query = "UPDATE CUSTOMER SET Table_Number='%d', Business_provided_till_now='%d' WHERE Phone_No='%s'" % (
            row["Table_num"], row["Business_provided"],row["Phone_num"])

        print(query)
        cur.execute(query)
        con.commit()
        query = "UPDATE TABLE_INFO SET Status='Occupied' WHERE Table_Number='%d'"%(row["Table_num"])
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def fireChef():  # DELETE Query
    try:
        row = {}
        row["Chef_ID"] = input("Chef ID: ")
        query0="SELECT Chef_ID FROM CHEF WHERE CHEF.Chef_ID='"+row["Chef_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The chef with chef id {row['Chef_ID']} doesn't exist in database")
            return
        query = "DELETE FROM CHEF WHERE Chef_ID='%s'" % (
            row["Chef_ID"])
 
        print(query)
        cur.execute(query)
        con.commit()
 
        print("Database Updated & Chef fired")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def findEmptyTable():   # SELECT Query
    try:
        # Takes ticket details as input
        row = {}
        

        query = "SELECT TABLE_INFO.Table_Number as tn , Section_Type FROM TABLE_INFO WHERE TABLE_INFO.Status='Not occupied'"

        print(query)
        cur.execute(query)
        con.commit()

        output = cur.fetchall()
        for x in output:
            print(f"\nTable No:{x['tn']}  Section Type:{x['Section_Type']}\n")

        print("Retrieved From Database")

    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return

def insertBrings():
    try:
        row={}
        row["wi"]=input("Give waiter Id:")
        row["on"]=int(input("Give order number:"))
        row["pn"]=input("Give phone number of customer:")
        row["dt"]=input("Give date:")
        row["ci"]=input("Give chef id:")
        row["tn"]=int(input("Give table no:"))
        query="INSERT INTO BRINGS(Waiter_ID,Order_Number,Customer_Phone_No,Date,Chef_ID,Table_Number) VALUES('%s','%d','%s','%s','%s','%d')" %(row["wi"],row["on"],row["pn"],row["dt"],row["ci"],row["tn"])
        cur.execute(query)
        con.commit()
        print("Inserted to database")
    except Exception as e:
        con.rollback()
        print("Failed to add to database")
        print(">>>>>>>>>>>>>", e)
    return

def insertGives():
    try:
        row={}
        row["wi"]=input("Give waiter Id:")
        row["on"]=int(input("Give order number:"))
        row["pn"]=input("Give phone number of customer:")
        row["dt"]=input("Give date:")
        query="INSERT INTO GIVES(Phone_No,Order_Number,Date,Waiter_ID) VALUES('%s','%d','%s','%s')" %(row["pn"],row["on"],row["dt"],row["wi"])
        cur.execute(query)
        con.commit()
        print("Inserted to database")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return





# def removeCustomer():
#     try:
#         row = {}
#         row["Phone_No"] = input("Customer Phone Number: ")

#         query = "DELETE FROM CUSTOMER WHERE Phone_No='%s'" % (row["Phone_No"])

#         print(query)
#         cur.execute(query)
#         con.commit()

#         print("Customer Removed Successfully")

#     except Exception as e:
#         con.rollback()
#         print("Failed to delete customer from database")
#         print(">>>>>>>>>>>>",e)
#     return

def FireWaiter():
    try:
        row = {}
        row["Waiter_ID"] = input("Waiter ID: ")
        query0="SELECT Waiter_ID FROM WAITER WHERE WAITER.Waiter_ID='"+row["Waiter_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The waiter with waiter id {row['Waiter_ID']} doesn't exist in database")
            return
        query = "DELETE FROM WAITER WHERE Waiter_ID='%s'" % (row["Waiter_ID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Waiter Removed Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to delete Waiter from database")
        print(">>>>>>>>>>>>",e)
    return

def removeDish():
    try:
        row = {}
        row["Name"] = input("Dish Name: ")
        query0="SELECT Name FROM DISH WHERE DISH.Name='"+row["nm"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The table with table no {row['Table_num']} doesn't exist in database")
            return
        query = "DELETE FROM DISH WHERE Name='%s'" % (row["Name"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Dish Removed Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to Dish from database")
        print(">>>>>>>>>>>>",e)
    return

def removeSupplier():
    try:
        row = {}
        row["Supplier_ID"] = input("Supplier ID: ")
        query0="SELECT Supplier_ID FROM SUPPLIER WHERE SUPPLIER.Supplier_ID='"+row["Supplier_ID"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The supplier with supplier_id :{row['Supplier_ID']} doesn't exist in database")
            return
        query = "DELETE FROM SUPPLIER WHERE Supplier_ID='%s'" % (row["Supplier_ID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Supplier Removed Successfully")

    except Exception as e:
        con.rollback()
        print("Failed to delete Supplier from database")
        print(">>>>>>>>>>>>",e)
    return



def checkWhoGaveOrderByDate():
    try:
        row={}
        row["pn"]=input("Give phone number of customer:")
        row["dt"]=input("Give date for which you wanna check:")
        query="SELECT WAITER.Fname as wf , WAITER.Mname as wm ,WAITER.Lname as wl,WAITER.Waiter_ID as wid, CHEF.Fname as cf , CHEF.Mname as cm , CHEF.Lname as cl, CHEF.Chef_ID as cid FROM ((BRINGS INNER JOIN WAITER ON BRINGS.Waiter_ID=WAITER.Waiter_ID) INNER JOIN CHEF ON BRINGS.Chef_ID=CHEF.Chef_ID) WHERE BRINGS.Customer_Phone_No='"+row["pn"]+"' AND BRINGS.Date='"+row["dt"]+"'"
        cur.execute(query)
        con.commit()
        output=cur.fetchall()
        for x in output:
            print(f"\nWaiter named: {x['wf']} {x['wm']} {x['wl']} Waiter ID:{x['wid']}  brought order from chef named: {x['cf']} {x['cm']} {x['cl']}  Chef ID:{x['cid']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def changePriceOfDish():
    try:
        row={}
        row["nm"]=input("Give name of dish whose price you want to change:")
        row["new"]=int(input("Give new price of dish:"))
        query0="SELECT Name FROM DISH WHERE DISH.Name='"+row["nm"]+"'"
        cur.execute(query0)
        con.commit()
        output0=cur.fetchall()
        if len(output0)==0:
            print(f"The table with table no {row['Table_num']} doesn't exist in database")
            return
        query="UPDATE DISH SET PRICE='"+str(row["new"])+"' WHERE Name='"+row["nm"]+"'"
        cur.execute(query)
        con.commit()
        print("Price changed")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return


def checkDishWithKeywordInName():
    try:
        row={}
        row["nm"]=input("Give keyword you want to search in name:")
        query="SELECT Name,Cuisine,Price FROM DISH WHERE Name LIKE '%"+row["nm"]+"%'"
        cur.execute(query)
        con.commit()
        output=cur.fetchall()
        for x in output:
            print(f"\nName:{x['Name']}  Cuisine:{x['Cuisine']}  Price:{x['Price']}\n")
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insertCustomer()
    elif(ch == 2):
        insertTable()
    elif(ch == 3):
        insertChef()
    elif(ch == 4):
        updateTableStatus()
    elif(ch == 5):
        updateCustomer_Table_BusinessProvided()
    elif(ch == 6):
        fireChef()
    elif(ch == 7):
        insertSupplier()
    elif(ch == 8):
        findEmptyTable()
    elif(ch == 9):
        insertWaiter()
    elif(ch == 10):
        insertDish()
    elif(ch == 11):
        insertIngredients()
    elif(ch == 12):
        highestSaleDish()
    elif(ch == 13):
        allOrdersOfaCustomers()
    elif(ch == 14):
        allDishesOfCategory()
    elif(ch == 15):
        getTotalSalaryOfChefs()
    elif(ch == 16):
        maxTotalPrice()
    elif(ch==17):
        getDishByKeyword()
    elif(ch==18):
        getCustomerByLastName()
    elif(ch==19):
        giveTop5dishes_ac_to_feedback()
    elif(ch==20):
        giveTotalRevenue_month()
    elif(ch==21):
        bestWaiterOftheMonth()
    elif(ch==22):
        insertCombo()
    elif(ch==23):
        insertNewOrder()
    elif(ch==24):
        insertGives()
    elif(ch==25):
        insertBrings()
    elif(ch==26):
        checkWhoGaveOrderByDate()
    elif(ch==27):
        AssignMentor()
    elif(ch==28):
        ChangeWaiterSalary()
    elif(ch==29):
        ChangeChefSalary()
    elif(ch==30):
        FireWaiter()
    elif(ch==31):
        removeSupplier()
    elif(ch==32):
        checkDishWithKeywordInName()
    elif(ch==33):
        removeDish()
    elif(ch==34):
        changePriceOfDish()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user='user',
                              password='password',
                              db='final_restaurant',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)

                print("1. Add new customer")
                print("2. Add new table")
                print("3. Add a new Chef")
                print("4. Update Status of Table")
                print(
                    "5. Update Customer Business provided & Table Number with Table's status")
                print("6. Fire a Chef")
                print("7. Insert a new Supplier")
                print("8. Find all tables which are empty")
                print("9. Insert new waiter")
                print(
                    "10. Insert new Dish")
                print(
                    "11. Insert new Ingredient")
                print(
                    "12. Get the name of Dish with highest sale")
                print(
                    "13. All orders of a customer")
                print("14. All dishes of a particular category")
                print(
                    "15. Get total salary being given to all Chefs")
                print(
                    "16. Get max total price of an order")
                print(
                    "17. Get dish by keyword (please give keyword in lowercase)")
                print(
                    "18. Get all customers with specific last name")
                print(
                    "19. Get top 5 popular dishes according to feedback")
                print(
                    "20. Get total revenue month wise")
                print(
                    "21. Best waiter of the month")
                print(
                    "22. Insert new combo")
                print(
                    "23. Insert new order")
                print(
                    "24. Insert new gives instance")
                print(
                    "25. Insert new brings instance")
                print(
                    "26. Get info that who bought order from whom on particular date")
                print(
                    "27. Assign a mentor to a waiter")
                print(
                    "28. Change salary of a waiter")
                print(
                    "29. Change salary of a chef")
                print(
                    "30. Remove waiter from database")
                print(
                    "31. Remove supplier from database")
                print(
                    "32. Give dishes with keyword in name")
                print(
                    "33. Delete dish by name")
                print(
                    "34. Update price of a dish")
                print("35. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 35:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")