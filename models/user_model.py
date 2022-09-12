import mysql.connector
import json
class user_model:
    def __init__(self):
         # connection code
        try:
           self.con = mysql.connector.connect(host='localhost', user='root', password='Captain@7337', database='flask_crud')
           self.con.autocommit = True
           self.cur = self.con.cursor(dictionary=True)
           print('connection successful')  
        except:
            print('some error')
        
    def user_getall_model(self):
        # query logic code
        self.cur.execute('SELECT * FROM users')
        results = self.cur.fetchall()
        if(len(results) > 0):
            return json.dumps(results)
        else:
            return "Not Found"
    def user_addone_model(self, data):
       # INSERT INTO `flask_crud`.`users` (`name`, `email`, `phone`, `role`, `password`) VALUES ('ramesh', 'ramesh@gmail.com', '7337022673', '1', 'Captain@7337');
        print(data)
        try:
            self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
            
            return "user created"
        except TypeError:
            print("TypeError: Check list of indices")
        
        