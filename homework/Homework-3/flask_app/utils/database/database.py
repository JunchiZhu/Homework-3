import mysql.connector
import glob
import json
import csv
from io import StringIO
import itertools
import hashlib
import os
import cryptography
from cryptography.fernet import Fernet
from math import pow

class database:

    def __init__(self, purge = False):

        # Grab information from the configuration file
        self.database       = 'db'
        self.host           = '127.0.0.1'
        self.user           = 'master'
        self.port           = 3306
        self.password       = 'master'
        self.tables         = ['institutions', 'positions', 'experiences', 'skills','feedback', 'users']
        
        # NEW IN HW 3-----------------------------------------------------------------
        self.encryption     =  {   'oneway': {'salt' : b'averysaltysailortookalongwalkoffashortbridge',
                                                 'n' : int(pow(2,5)),
                                                 'r' : 9,
                                                 'p' : 1
                                             },
                                'reversible': { 'key' : '7pK_fnSKIjZKuv_Gwc--sZEMKn2zc8VvD6zS96XcNHE='}
                                }
        #-----------------------------------------------------------------------------

    def query(self, query = "SELECT * FROM users", parameters = None):

        cnx = mysql.connector.connect(host     = self.host,
                                      user     = self.user,
                                      password = self.password,
                                      port     = self.port,
                                      database = self.database,
                                      charset  = 'latin1'
                                     )


        if parameters is not None:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query, parameters)
        else:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query)

        # Fetch one result
        row = cur.fetchall()
        cnx.commit()

        if "INSERT" in query:
            cur.execute("SELECT LAST_INSERT_ID()")
            row = cur.fetchall()
            cnx.commit()
        cur.close()
        cnx.close()
        return row

    def createTables(self, purge=False, data_path = 'flask_app/database/'):
        ''' FILL ME IN WITH CODE THAT CREATES YOUR DATABASE TABLES.'''

        #should be in order or creation - this matters if you are using forign keys.
         
        if purge:
            for table in self.tables[::-1]:
                self.query(f"""DROP TABLE IF EXISTS {table}""")
            
        # Execute all SQL queries in the /database/create_tables directory.
        for table in self.tables:
            
            #Create each table using the .sql file in /database/create_tables directory.
            with open(data_path + f"create_tables/{table}.sql") as read_file:
                create_statement = read_file.read()
            self.query(create_statement)

            # Import the initial data
            try:
                params = []
                with open(data_path + f"initial_data/{table}.csv") as read_file:
                    scsv = read_file.read()            
                for row in csv.reader(StringIO(scsv), delimiter=','):
                    params.append(row)
            
                # Insert the data
                cols = params[0]; params = params[1:] 
                self.insertRows(table = table,  columns = cols, parameters = params)
            except:
                print('no initial data')

    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        
        # Check if there are multiple rows present in the parameters
        has_multiple_rows = any(isinstance(el, list) for el in parameters)
        keys, values      = ','.join(columns), ','.join(['%s' for x in columns])
        
        # Construct the query we will execute to insert the row(s)
        query = f"""INSERT IGNORE INTO {table} ({keys}) VALUES """
        if has_multiple_rows:
            for p in parameters:
                query += f"""({values}),"""
            query     = query[:-1] 
            parameters = list(itertools.chain(*parameters))
        else:
            query += f"""({values}) """                      
        
        insert_id = self.query(query,parameters)[0]['LAST_INSERT_ID()']         
        return insert_id

    def getResumeData(self):
            # Pulls data from the database to genereate data like this:

            institutions = self.query("SELECT * FROM institutions")
            positions = self.query("SELECT * FROM positions")
            experiences = self.query("SELECT * FROM experiences")
            skills = self.query("SELECT * FROM skills")

            institution_dict = {}
            for i in institutions:
                 ins_id = i['inst_id']
                 institution_dict[ins_id] = i
                 institution_dict[ins_id].pop('inst_id')
                 positions = self.query(f"""SELECT * FROM positions WHERE inst_id = {ins_id}""")
                 position_dict = {}
                 for j in positions:
                     pos_id = j['position_id']
                     position_dict[pos_id] = j
                     position_dict[pos_id].pop('inst_id')
                     position_dict[pos_id].pop('position_id')
                     institution_dict[ins_id]['positions'] = position_dict
                     experiences = self.query(f"""SELECT * FROM experiences WHERE position_id = {pos_id}""")
                     experience_dict = {}
                     for k in experiences:
                         exp_id = k['experience_id']
                         experience_dict[exp_id] = k
                         experience_dict[exp_id].pop('experience_id')
                         experience_dict[exp_id].pop('position_id')
                         position_dict[pos_id]['experiences'] = experience_dict
                         skills = self.query(f"""SELECT * FROM skills WHERE experience_id = {exp_id}""")
                         skill_dict = {}
                         for l in skills:
                            ski_id = l['skill_id']
                            skill_dict[ski_id] = l
                            skill_dict[ski_id].pop('skill_id')
                            skill_dict[ski_id].pop('experience_id')
                            experience_dict[exp_id]['skills'] = skill_dict
            return institution_dict

    def insertFeedback(self, table='feedback',value4 = []):
        #   query = f"INSERT IGNORE INTO {table} ({','.join(columns)}) VALUES"
            query = f"""INSERT IGNORE INTO {table} (name,email,comment) VALUES"""
            query+="("
            for i in range(3):
                query+=f"""'{value4[i]}'"""
                if i != 2:
                    query+=','
            query+=")"
            self.query(query)


    def getFeedbackDate(self):
        feedback = self.query("SELECT * FROM feedback")
        return feedback


#######################################################################################
# AUTHENTICATION RELATED
#######################################################################################
    def createUser(self, email='me@email.com', password='password', role='user'):
        Users = self.query("SELECT * FROM users")
        query = f"""INSERT IGNORE INTO {'users'} (role,email,password) VALUES"""
        value = []
        value.append(role)
        value.append(email)
        password = self.onewayEncrypt(password)
        value.append(password)
        check = 0
        #[{'user_id': 1, 'role': 'owner', 'email': 'owner@email.com', 'password': 'password'}]
        for i in range(len(Users)):
            for item in Users[i].values():
                if item == email:
                    check+=1
        if check==0:
            query+="("
            for i in range(3):
                query+=f"""'{value[i]}'"""
                if i != 2:
                    query+=','
            query+=")"
            self.query(query)




    def authenticate(self, email='me@email.com', password='password'):
#     [{'user_id': 1, 'role': 'owner', 'email': 'owner@email.com',
#     'password': '842f7ec4b7f763388931153324c696b7d9c3e230d4d196e4d0b43a6ec950e273c84e648a0f78693aeb49f1f3893e1896d6582d59fdc1d84632f5f98740e1d465'}]
        Users2 = self.query("SELECT * FROM users")
        password = self.onewayEncrypt(password)
        for i in range(len(Users2)):
            if Users2[i]["email"] == email and  Users2[i]["password"] == password:
                return True
        return False


    def onewayEncrypt(self, string):
        encrypted_string = hashlib.scrypt(string.encode('utf-8'),
                                          salt = self.encryption['oneway']['salt'],
                                          n    = self.encryption['oneway']['n'],
                                          r    = self.encryption['oneway']['r'],
                                          p    = self.encryption['oneway']['p']
                                          ).hex()
        return encrypted_string


    def reversibleEncrypt(self, type, message):
        fernet = Fernet(self.encryption['reversible']['key'])
        
        if type == 'encrypt':
            message = fernet.encrypt(message.encode())
        elif type == 'decrypt':
            message = fernet.decrypt(message).decode()

        return message


