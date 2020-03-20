#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import pymysql

class link_db:
    def __init__(self):
        pass

    def Get_file(self, cmd_file):
        filename = os.path.basename(cmd_file)
        file = open(cmd_file)
        file1 = file.read()
        imp = re.findall(r"import\s\w+", file1, re.S)
        func = re.findall(r"def\sdo\w+", file1, re.S)

        func_all = []
        for i in func:
            j = i.strip('def')
            func_all.append(j)

        print(func_all)
        print(len(func_all))

        imp_arr = []
        for i in imp:
            j = i.strip('import')
            imp_arr.append(j)
        print(imp_arr)

        mydb = pymysql.connect(host="127.0.0.1", user="root", passwd="1234", database="class")

        cursor = mydb.cursor()
        cursor.execute("CREATE TABLE content ( packages VARCHAR(25), features VARCHAR(25))")

        for d in func_all:
            for f in imp_arr:
                sql = "INSERT INTO content (packages, features) VALUES (%s, %s)"
                val = (f,d)
        cursor.execute(sql, val)
        mydb.commit()




if __name__ == '__main__':
    link_db().Get_file("ppp_cmd.py")


