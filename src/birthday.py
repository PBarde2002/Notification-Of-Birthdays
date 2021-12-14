from datetime import date

today = date.today()
today_date= today.strftime("%Y-%m-%d")


with open("C://flask//new//Login-Page-With-Flask-HTML//src//birthdaydate.txt","r", encoding='utf8') as file: 
     data = file.readlines()
     for line in data:
        msg_date = line.split()
       
        if msg_date[0]==today_date:    
            print('hbd')
        else:
            pass

       
        
   
   

        
               
    
	
		    