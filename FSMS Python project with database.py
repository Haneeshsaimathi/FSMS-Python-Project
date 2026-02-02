# Idea Fruit Shop Display
# characters = Owner and Buyer

# OWNER: 
# Step1: Owner have to login in as Owner 
# Step2: Enter Password
# Step2: Owner have access to these nine options
#       Owner have 9 options to check about shop:
#                   1. Add New Fruits
#                   2. Modify Available kgs
#                   3. Modify Selling Price
#                   4. Modify Cost Price
#                   5. Check Profit
#                           1. Overall Shop Profit
#                           2. Fruit with Maximum Profit
#                           3. Fruit with Minimum Profit
#                           4. Exit
#
#                   6. Buyer number and Fruits
#                   7. All Customer Details
#                   8. Check Order Details
#                   9. Exit
#

# BUYER:
# Step1: Buyer have 3 options:
#                   1. Shopping
#                   2. Place the order
#                   3. Exit
#
# Step2: Choose Action
# Step3: Enter Customer Details
# Step4: Buyer have to perform any actions in both shopping and place the order
#       Buyer have 4 options for buyers:
#                   1. Add Fruit
#                   2. Remove Fruit
#                   3. View Cart
#                   4. Exit
#
#
# This works as a Interface, once it starts it wont stop. which means after every buyer or owner task, it always asks are you owner or buyer
#


import mysql.connector as db

con = db.connect (user = 'root', password = '*******',\
                  host = 'localhost', database = 'project')

cur = con.cursor()

cur = con.cursor()
cur_dict = con.cursor(dictionary=True,buffered=True)

cur.execute("update total_profit set over_all_profit = 0")
cur.execute("update menu set profit = 0")
cur.execute("delete from cart")
cur.execute("delete from buyer")
cur.execute("delete from order___")
con.commit()

 
while True:
    print()
    print('*' * 60)
    print('        Welcome to Haneesh Sai Fruit Shop  ')
    print('*' *60)
    while True:
        role = input('Are you Owner or Buyer: ').lower()
        if role == 'owner' or role == 'buyer':
            break
        print('Enter enter valid role') 

    if role =='owner':
            while True:
                ch = input('enter password: ')
                if ch == 'Haneesh':
                    break
                else:
                    print('Wrong password, try again')

            print()
            cur.execute('select * from menu')
            rows = cur.fetchall()
            print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10} {'original_price':<18} {'Profit':<15}")
            for row in rows:
                print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10} {row[3]:10} {row[4]:10}")
            print()

            while True:
                print()
                print("1. Add New Fruits")
                print("2. Modify Available_kgs")
                print("3. Modify Selling Price")
                print("4. Modify Cost Price")
                print("5. Check Profit")
                print("6. Specific Customer Details")
                print("7. All Customer Details")
                print("8. Check Order Details")
                print("9. Exit")


                print()
                while True:
                    try:
                        op = int(input("Which operation do you want to do: "))
                        break
                    except ValueError:
                        print('Please enter correct option')
                print()



                if op == 1:
                    ch = input('Enter new fruit name: ')
                    cur.execute("select name from menu where name = %s",[ch])
                    if cur.fetchone():
                        print('Fruit is Already in the store')
                    else:
                        akg = float(input('enter available kgs: '))
                        price = int(input('enter price: '))
                        original = int(input('enter original price: '))
                        cur.execute("insert into menu(name,available_kg,price,original_price) values(%s,%s,%s,%s)",[ch,akg,price,original])
                        cur.execute(f"alter table buyer add {ch} float default 0")
                        con.commit()
                        print('Fruit added succsessfully')
                        print()
                        cur.execute("select * from menu")
                        rows = cur.fetchall()
                        print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10} {'original_price':<18} {'Profit':<15}")
                        for row in rows:
                            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10} {row[3]:10} {row[4]:10}")
                        print()


                            
                if op == 2:
                    ch = input('Enter which fruit price you want to change: ')
                    cur.execute("select name from menu where name = %s",[ch])
                    if cur.fetchone():
                        available = int(input('Enter available kgs: '))
                        cur.execute("update menu set available_kg = %s where name = %s",[available,ch])
                        con.commit()
                        print('Available kgs changed sucessfully')
                        print()
                        cur.execute("select * from menu")
                        rows = cur.fetchall()
                        print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10} {'original_price':<18} {'Profit':<15}")
                        for row in rows:
                            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10} {row[3]:10} {row[4]:10}")
                        print()
                        
                    else:
                        print('That fruit is not available')



                        
                if op == 3:
                    ch = input('Enter fruit name to change price: ')
                    cur.execute("select name from menu where name = %s",[ch])
                    if cur.fetchone():
                        new_price = int(input('Enter new price: '))
                        cur.execute("update menu set price = %s where name = %s",[new_price,ch])
                        con.commit()
                        cur.execute("select * from menu")
                        rows = cur.fetchall()
                        print()
                        print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10} {'original_price':<18} {'Profit':<15}")
                        for row in rows:
                            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10} {row[3]:10} {row[4]:10}")
                        print()

                    else:
                        print('Fruit is not available')


                if op == 4:
                    ch = input('Enter fruit name to change price: ')
                    cur.execute("select name from menu where name = %s",[ch])
                    if cur.fetchone():
                        new_price = int(input('Enter new cost price: '))
                        cur.execute("update menu set original_price = %s where name = %s",[new_price,ch])
                        con.commit()
                        cur.execute("select * from menu")
                        rows = cur.fetchall()
                        print()
                        print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10} {'original_price':<18} {'Profit':<15}")
                        for row in rows:
                            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10} {row[3]:10} {row[4]:10}")
                        print()

                    else:
                        print('Fruit is not available')
                    


                    
                if op == 5:

                    while True:
                        print()
                        print("1. Shop Overall Profit")
                        print("2. Fruit with Maximum Profit")
                        print("3. Fruit with Minimum Profit")
                        print("4. Exit")
                        print()
                        while True:
                            try:
                                select = int(input("What you want to do: "))
                                break
                            except ValueError:
                                print('Enter correct option')

                        if select == 1:              
                            cur.execute("select sum(over_all_profit) from total_profit")
                            profit_row = cur.fetchone()
                            profit = profit_row[0] if profit_row else 0
                            print('Total profit:',profit)

                        if select == 2:
                            cur.execute("select name,profit from menu where profit =  (select max(Profit) from menu where profit > 0)")
                            res = cur.fetchall()
                            print("Fruit with Maximum Profit: ")
                            if not res:
                                print("No profit from any fruit")
                            else:
                                for i in res:
                                    print(i[0],':',i[1])

                        if select == 3:
                            cur.execute("select name,profit from menu where profit =  (select min(Profit) from menu)")
                            res = cur.fetchall()
                            print("Fruit with Minimum Profit: ")
                            for i in res:
                                print(i[0], ':',i[1])

                        if select == 4:
                            print("prrofit Section Closed Sucessfully")
                            break

                if op == 6:
                    ch = input("Enter buyer phone number: ")
                    cur_dict.execute("select * from buyer where phone = %s",[ch])
                    rows = cur_dict.fetchall()

                    if rows:
                        for row in rows:
                            print("\nBuyer:", row['phone'])
                            print("\nDate:", row['date'])
                            print("Fruits bought:")
                            for col, val in row.items():
                                if col not in('phone','date') and val not in (None, 0, ''):
                                    print(col, ":", val)
                    else:
                        print('No such buyer in history')



                if op == 7:
                    cur_dict.execute("select * from buyer")
                    rows = cur_dict.fetchall()

                    if rows:
                        for row in rows:
                            print("\nBuyer:",row['phone'])
                            print("\nDate:",row['date'])
                            print("Fruits bought:")
                            for col,val in row.items():
                                if col not in ('phone','date') and val not in (None,0,''):
                                    print(col,':',val)
                    else:
                        print('No buyers in history')



                if op == 8:
                    cur_dict.execute("select * from order___")
                    rows = cur_dict.fetchall()

                    if rows:
                        for row in rows:
                            print("\nBuyer:",row['mobile'])
                            print("Order Date:",row['order_date'])
                            print("Delivery Date:",row['delivery_date'])
                            print("Fruits ordered:")
                            print(row['items'], ':',row['required_kgs'], "kgs")
                            print("Price:",row['price'])
                            
                    else:
                        print('No Orders')

                
                if op == 9:
                    print("Exiting Owner Section......")
                    print("Owner Section Closed Sucessfully")
                    break






    if role == 'buyer':
        from datetime import datetime
        date = datetime.now().date()

        while True:
            print()
            print('*' *60)
            print('         Welcome to Haneesh Sai Fruit Shop ')
            print('*' *60)
            print()
            print()
            print("1. Shopping")
            print("2. Place Order on Specific Date")
            print("3. Exit")
            print()

            while True:
                try:
                    select = int(input("What you want to do: "))
                    break
                except ValueError:
                    print('Enter correct option')

                    
            if select == 1:
                    
                while True:
                    try:
                        phone = int(input('Enter phone number: '))
                        if len(str(phone)) == 10:
                            break
                        print('enter correct phone number')
                    except:
                        print('enter correct phone number')
                    
                print()
                
                cur.execute("insert into buyer(phone) values(%s)",[phone])
                con.commit()

                
                cur.execute('select * from menu')
                rows = cur.fetchall()
                print(f"{'Name':<10} {'Available_kg':<15} {'Price':<10}")
                for row in rows:
                    print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
                print()

                while True:
                    print()
                    print("1. Add Fruits")
                    print("2. Remove Fruits")
                    print("3. View Cart")
                    print("4. Exit")


                    while True:                
                        try:
                            select = int(input("what you want to do: "))
                            break
                        except ValueError:
                            print('Enter correct option')
                        
                    if select in(1,2,3,4):

                        if select == 1:
                            fruit = input("which fruit you want to buy: ")
                            cur.execute("select name from menu where name = %s",[fruit])
                            if cur.fetchone():
                                kg = float(input('Enter how many kgs you want: '))
                                cur.execute("select available_kg from menu where name = %s",[fruit])
                                row = cur.fetchone()
                                cnt = row[0] if row else 0
                                
                                if cnt >= kg:

                                    cur.execute("select fruit from cart where fruit = %s",[fruit])
                                    if cur.fetchone():
                                        cur.execute("select price from menu where name = %s",[fruit])
                                        price = cur.fetchone()[0]
                                        cur.execute("update cart set kgs_bought = kgs_bought + %s where fruit = %s",[kg,fruit])


                                        cur.execute("update menu set available_kg = available_kg - %s where name = %s",[kg,fruit])
                                        cur.execute("update cart set price = price + %s where fruit = %s",[price*kg,fruit])

                                        cur.execute("select original_price from menu where name = %s",[fruit])
                                        res = cur.fetchone()
                                        pr_price = res[0] if res else 0

                                        profit_per_kg = price - pr_price
                                        
                                        cur.execute("update total_profit set over_all_profit = ifnull(over_all_profit,0) + %s where profit = profit",[profit_per_kg * kg])
                                        cur.execute("update menu set profit = ifnull(profit,0) + %s where name = %s",[profit_per_kg * kg,fruit])
         
                                        query = f"update buyer set {fruit} = ifnull({fruit},0) + %s where phone = %s"
                                        cur.execute(query,[kg,phone])
                                        con.commit()
                                        
                                        cur.execute("select sum(price) from cart")
                                        total = cur.fetchone()[0] or 0
                                        print('Your total bill upto this is:',total)
                                        
                                        
                                    
                                    else:
                                        cur.execute("select price from menu where name = %s",[fruit])
                                        price = cur.fetchone()[0]
                                        

                                        cur.execute("insert into cart(fruit,kgs_bought,price) values(%s,%s,%s)",[fruit,kg,price*kg])
                                        cur.execute("update menu set available_kg = available_kg - %s where name = %s",[kg,fruit])

                                        

                                        
                                        query = f"update buyer set {fruit} = ifnull({fruit},0) + %s where phone = %s"
                                        cur.execute(query, [kg, phone])

                                        cur.execute("select original_price from menu where name = %s",[fruit])
                                        res = cur.fetchone()
                                        pr_price = res[0] if res else 0

                                        profit_per_kg = price - pr_price


                                        
                                        cur.execute("update total_profit set over_all_profit = ifnull(over_all_profit,0) + %s where profit = profit",[profit_per_kg * kg])
                                        cur.execute("update menu set profit = ifnull(profit,0) + %s where name = %s",[profit_per_kg * kg,fruit])

                                        cur.execute("update buyer set date = %s where phone = %s",[date,phone])         
                                        con.commit()
                                        
                                        cur.execute("select sum(price) from cart")
                                        total = cur.fetchone()[0] or 0
                                        print('Your total bill upto this is:',total)

                                    
                                else:
                                    print('That much of quantity not available')
                                         

                            else:
                                print('That fruit is not available')



                                    
                                    
                        if select == 2:
                            fruit = input("which fruit you want to remove: ")
                            cur.execute("select fruit from cart where fruit = %s",[fruit])
                            if cur.fetchone():
                                kg = float(input('Enter how many kgs you want to remove: '))
                                cur.execute("select kgs_bought from cart where fruit = %s",[fruit])
                                row = cur.fetchone()
                                original_bought = row[0] if row else 0
                                
                                if kg > original_bought:
                                    print("You didn't but that much kgs so enter valid kgs")
                                    
                                if kg == original_bought:
                                    cur.execute("update cart set kgs_bought = kgs_bought - %s where fruit = %s",[kg,fruit])
                                    
                                    
                                    cur.execute("update menu set available_kg = available_kg + %s where name = %s",[kg,fruit])
                                    cur.execute("delete from cart where fruit = %s",[fruit])

                        
                                    cur.execute(f"update buyer set {fruit} = greatest({fruit} - %s,0) where phone = %s",[kg,phone])

                                    cur.execute("select original_price from menu where name = %s",[fruit])
                                    res = cur.fetchone()
                                    pr_price = res[0] if res else 0

                                    cur.execute("select price from menu where name =%s",[fruit])
                                    sp = cur.fetchone()[0]
                                    profit_per_kg = sp - pr_price
                                    cur.execute("update total_profit set over_all_profit = over_all_profit - %s where profit = profit",[profit_per_kg * kg])
                                    cur.execute("update menu set profit = profit - %s where name = %s",[profit_per_kg * kg,fruit])
                                    
                                    con.commit()
                                    cur.execute("select sum(price) from cart")
                                    total = cur.fetchone()[0] or 0
                                    print('Your total bill upto this is:',total)

                                    con.commit()


                                if kg < original_bought:
                                    cur.execute("update cart set kgs_bought = kgs_bought - %s where fruit = %s",[kg,fruit])
                                    cur.execute("update menu set available_kg = available_kg + %s where name = %s",[kg,fruit])

                                    cur.execute("select price from menu where name = %s",[fruit])
                                    price = cur.fetchone()[0]
                                    cur.execute("update cart set price = kgs_bought * %s where fruit = %s",[price,fruit])

                                    cur.execute("select original_price from menu where name = %s",[fruit])
                                    res = cur.fetchone()
                                    pr_price = res[0] if res else 0
                                    
                                    cur.execute("select price from menu where name =%s",[fruit])
                                    sp = cur.fetchone()[0]
                                    profit_per_kg = sp - pr_price
                                    
                                    cur.execute("update total_profit set over_all_profit = over_all_profit - %s where profit = profit",[profit_per_kg* kg])

                                    cur.execute(f"update buyer set {fruit} = greatest({fruit} - %s,0) where phone = %s",[kg,phone])
                                    
                                    con.commit()
                                    cur.execute("select sum(price) from cart")
                                    total = cur.fetchone()[0] or 0
                                    print('Your total bill upto this is:',total)


                            else:
                                print("You didn't buy that fruit")

                            


                        if select == 3:
                            cur.execute("select * from cart")
                            rows = cur.fetchall()
                            print(f"{'fruit':<10} {'kgs_bought':<15} {'Price':<10}")
                            for row in rows:
                                print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
                            print()
                            cur.execute("select sum(price) from cart")
                            row = cur.fetchone()
                            total = row[0] if row else 0
                            print('Your total bill upto this is:',total)
                                         



                        if select == 4:
                            cur.execute("select sum(price) from cart")
                            total = cur.fetchone()[0] or 0
                            print()
                            print('Haneesh Sai Fruit Shop')
                            print('-'*45)
                            print()
                            print('Tax:',float(total)*0.1)
                            print('Discount:',float(total)*0.1)
                            print('-'*45)
                            print()
                            cur.execute("select * from cart")
                            rows = cur.fetchall()
                            print(f"{'fruit':<10} {'kgs_bought':<15} {'Price':<10}")
                            for row in rows:
                                print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")
                            print('-'*45)
                            print()
                            cur.execute("select count(*) from cart")
                            res = cur.fetchone()[0] or 0
                            cur.execute("select sum(kgs_bought) from cart")
                            kgs = cur.fetchone()
                            nkgs = kgs[0] if kgs[0] is not None else 0 
                            print('Items: ',res,'  Quantity: ',nkgs,'  Value: ',total)
                            print()
                            from datetime import datetime
                            x = datetime.now().date()
                            print(f'Thank you for visiting            Date:{x}')
                            cur.execute("delete from cart")
                            con.commit()
                            print()
                            break
                        
                    else:
                        print('Select Correct Option')
                    

            if select == 2:
                            
                while True:
                    try:
                        phone = int(input('Enter phone number: '))
                        if len(str(phone)) == 10:
                            break
                        print('enter correct phone number')
                    except:
                        print('enter correct phone number')
                    
                print()

                
                cur.execute('select * from menu')
                rows = cur.fetchall()
                print(f"{'Name':<10} {'Price':<10}")
                for row in rows:
                    print(f"{row[0]:<10} {row[2]:<10}")
                print()

                while True:
                    print()
                    print("1. Add Fruits")
                    print("2. Remove Fruits")
                    print("3. View Cart")
                    print("4. Exit")


                    while True:                
                        try:
                            select = int(input("what you want to do: "))
                            break
                        except ValueError:
                            print('Enter correct option')
                        
                    if select in(1,2,3,4):                     
                        if select == 1:
                            
                            while True:
                                try:
                                    fruit = input("which fruit you want to buy: ")
                                    break
                                except ValueError:
                                    print('Please enter digits not letters or special characters')
                                    
                            cur.execute("select name from menu where name = %s",[fruit])
                            
                            if cur.fetchone():
                                while True:
                                    try:
                                        kg = float(input('Enter how many kgs you want: '))
                                        break
                                    except ValueError:
                                        print('Please enter digits not letters or special characters')

                                        
                                from datetime import datetime, date
                                date = date.today()
                

                                while True:
                                    d_date = input("Enter delivery date (DD-MM-YYYY): ").strip()

                                    try:
                                        user_date = datetime.strptime(d_date, "%d-%m-%Y").date()
                                        if user_date <= date:
                                            print("Please enter a valid date")
                                            continue
                                        break
                                    except:
                
                                        continue

                                cur.execute("select items from order___ where items = %s",[fruit])
                                if cur.fetchone():
                                    cur.execute("update order___ set price = price + %s where fruit = %s",[price*kg,fruit])
                                    cur.execute("update order___ set required_kgs = required_kgs + %s where items = %s",[kg,fruit])

                                    
                                else:
        
                                    cur.execute("select price from menu where name = %s",[fruit])
                                    price = cur.fetchone()[0]
                                    cur.execute("insert into order___ (mobile,order_date,delivery_date,items,required_kgs,price) values(%s,%s,%s,%s,%s,%s)",[phone,date,user_date,fruit,kg,price*kg,])
        
                                 
                            else:
                                print('Sorry, Fruit is not available')


                        if select == 2:
                            fruit = input("Which fruit you want to remove: ")
                            cur.execute("select items from order___ where items = %s",[fruit])
                            if cur.fetchone():
                                while True:
                                    try:
                                        kg = float(input('Enter how many kgs you want to remove: '))
                                        break
                                    except ValueError:
                                        print('Enter required kgs, dont use letters or special characters to enter kgs')
                                        
                                cur.execute("select required_kgs from order___ where items = %s",[fruit])
                                res = cur.fetchone()
                                ava_kg = res[0] if res else 0

                                if ava_kg < kg:
                                    print('Your ordered quantity is less so enter valid data')

                                if ava_kg == kg:
                                    cur.execute("delete from order___ where items = %s",[fruit])
                                    cur.execute("select sum(price) from order___")
                                    row = cur.fetchone()
                                    total = row[0] if row else 0
                                    print('Your total bill upto this is:',total)

                                if  ava_kg > kg:
                                    cur.execute("update order___ set required_kgs = required_kgs - %s",[kg])
                                    cur.execute("select price from menu where name = %s",[fruit])
                                    price = cur.fetchone()[0]
                                    cur.execute("update order___ set price = required_kgs * %s where items = %s",[price,fruit])


                                    cur.execute("select sum(price) from order___")
                                    row = cur.fetchone()
                                    total = row[0] if row else 0
                                    print('Your total bill upto this is:',total)


                            else:
                                print("You didnt order that fruit")

                                
                        if select == 3:

                            cur.execute("select * from order___")
                            rows = cur.fetchall()
                            print(f"{'items':<10} {'required_kgs':<15} {'delivery_date':<10}")
                            for row in rows:
                                print(f"{row[3]:<10} {row[4]:<15} {(row[2].strftime('%d-%m-%Y') if row[2] else ''):<10}")
                            print()
                            
                            cur.execute("select sum(price) from order___")
                            row = cur.fetchone()
                            total = row[0] if row else 0
                            print('Your total bill upto this is:',total)

                            
                        if select == 4:
                            print()
                            print("Thank you for placing order, we will contact you soon")
                            from datetime import datetime
                            x = datetime.now().date()
                            print(f'Date:{x}')
                            break

                            
                    else:
                        print('Enter Correct Option')




            if select == 3:
                
                attempts = 0
                while attempts < 3:
                    ch = input("Enter password: ")
                    if ch == 'Haneesh':
                        print("\nExiting Customer Section......")
                        print("Customer Section Closed Successfully\n")
                        break
                    else:
                        attempts += 1
                        print('This can be accessed by only owner, if you are owner enter correct password')

                break



cur.close()
con.close()
