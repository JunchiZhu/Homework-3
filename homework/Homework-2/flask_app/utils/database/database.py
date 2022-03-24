import mysql.connector
import glob
import json
import csv
import os
from io import StringIO
import itertools
import datetime

class database:

    def __init__(self, purge = False):

        # Grab information from the configuration file
        self.database       = 'db'
        self.host           = '127.0.0.1'
        self.user           = 'master'
        self.port           = 3306
        self.password       = 'master'

    def query(self, query = "SELECT CURDATE()", parameters = None):

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

    def about(self, nested=False):
        query = """select concat(col.table_schema, '.', col.table_name) as 'table',
                          col.column_name                               as column_name,
                          col.column_key                                as is_key,
                          col.column_comment                            as column_comment,
                          kcu.referenced_column_name                    as fk_column_name,
                          kcu.referenced_table_name                     as fk_table_name
                    from information_schema.columns col
                    join information_schema.tables tab on col.table_schema = tab.table_schema and col.table_name = tab.table_name
                    left join information_schema.key_column_usage kcu on col.table_schema = kcu.table_schema
                                                                     and col.table_name = kcu.table_name
                                                                     and col.column_name = kcu.column_name
                                                                     and kcu.referenced_table_schema is not null
                    where col.table_schema not in('information_schema','sys', 'mysql', 'performance_schema')
                                              and tab.table_type = 'BASE TABLE'
                    order by col.table_schema, col.table_name, col.ordinal_position;"""
        results = self.query(query)
        if nested == False:
            return results

        table_info = {}
        for row in results:
            table_info[row['table']] = {} if table_info.get(row['table']) is None else table_info[row['table']]
            table_info[row['table']][row['column_name']] = {} if table_info.get(row['table']).get(row['column_name']) is None else table_info[row['table']][row['column_name']]
            table_info[row['table']][row['column_name']]['column_comment']     = row['column_comment']
            table_info[row['table']][row['column_name']]['fk_column_name']     = row['fk_column_name']
            table_info[row['table']][row['column_name']]['fk_table_name']      = row['fk_table_name']
            table_info[row['table']][row['column_name']]['is_key']             = row['is_key']
            table_info[row['table']][row['column_name']]['table']              = row['table']
        return table_info



    def createTables(self, purge=False, data_path = 'flask_app/database/'):
        print('I create and populate database tables!!')
        sqlTables  = ['institutions.sql', 'positions.sql', 'experiences.sql', 'skills.sql','feedback.sql']
        csvTables  = ['institutions.csv', 'positions.csv', 'experiences.csv', 'skills.csv']
        size = len(sqlTables)
        sql_list = os.listdir(data_path+'/create_tables/')
        csv_list = os.listdir(data_path+'/initial_data/')

        if purge == True:
            self.query(" DROP TABLE IF EXISTS feedback ")
            self.query(" DROP TABLE IF EXISTS skills ")
            self.query(" DROP TABLE IF EXISTS experiences ")
            self.query(" DROP TABLE IF EXISTS positions ")
            self.query(" DROP TABLE IF EXISTS institutions ")


        counter = 0
        while (counter<size):
            sqlFile = sqlTables[counter]
            filename = (data_path + 'create_tables/' + sqlFile)
            file1 = open(filename)
            sql = file1.read()
            # make table

            self.query(sql)
            file1.close()
            # import csv data and call insertRows function
            index = sqlFile.index(".")
            tableName = sqlFile[:index]
            if (tableName+".csv") in csvTables:
                csvFilePos = csvTables.index(tableName+".csv")
                csvFile = (data_path + 'initial_data/' + csvTables[csvFilePos])
                file2 = open(csvFile)
                Lines = file2.readlines()
                file2.close()

                flag = 0
                para2= [[]]
                for i in Lines:
                    if flag == 0:
                        name = i.replace('"','')
                        para1 = name.split(",")
                        flag += 1
                    else:
                        comp = i.replace('"','')
                        para = comp.split(",")
                        para2.append(para)
                para2.pop(0)
                print("!" + tableName)
                self.insertRows(tableName,para1,para2)
            print(tableName)
            counter += 1
        experiences = self.query("SELECT * FROM experiences")
        print(experiences)





    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        print('I insert things into the database.')
        query = f"INSERT IGNORE INTO {table} ({','.join(columns)}) VALUES"
        for i in range(len(parameters)):
            query+='('
            for j in range(len(parameters[i])):
                if parameters[i][j] == "NULL" or parameters[i][j] == 'NULL\n':
                    query+="NULL"
                else:
                    query+= f"'{parameters[i][j]}'"
                if j != len(parameters[i])-1:
                    query+=','
            query+=")"
            if i != len(parameters)-1:
                query+=','
        print(table)
        self.query(query)


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


#
# [{'experience_id': 1, 'position_id': 1, 'name': 'Game Development', 'description': 'Design a simple game by using C++', 'hyperlink': 'https://www.linkedin.com/in/junchi-zhu-65b4b5190/', 'start_date': datetime.date(2020, 1, 1), 'end_date': None},
# {'experience_id': 2, 'position_id': 2, 'name': 'Application Development', 'description': 'Design a simple Phone game by using C++', 'hyperlink': 'https://www.linkedin.com/in/junchi-zhu-65b4b5190/', 'start_date': datetime.date(2021, 1, 1), 'end_date': datetime.date(2022, 1, 1)},
#  {'experience_id': 3, 'position_id': 3, 'name': 'Design self made movie application', 'description': 'Design a movie maker application by using C++', 'hyperlink': 'https://www.linkedin.com/in/junchi-zhu-65b4b5190/', 'start_date': datetime.date(2021, 1, 1), 'end_date': datetime.date(2021, 12, 31)},
#  {'experience_id': 4, 'position_id': 4, 'name': 'Design iphone SE case', 'description': 'Using Fusion 360 design iphone SE case', 'hyperlink': 'https://www.linkedin.com/in/junchi-zhu-65b4b5190/', 'start_date': datetime.date(2019, 1, 1), 'end_date': datetime.date(2020, 1, 1)}]
