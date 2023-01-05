#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install mysql-connector-python')


# In[7]:


import mysql.connector as conn


# In[10]:


mydb = conn.connect(host = 'localhost', user = 'root', passwd = 'Gate@2015')  #connection variable


# 

# In[17]:


cursor = mydb.cursor()    #pointer 


# In[18]:


cursor.execute("show databases")


# In[19]:


cursor.fetchall()


# In[24]:


cursor.execute("create database scaler1")


# In[29]:


cursor.execute("use scaler1")


# In[50]:


cursor.execute('CREATE TABLE sales1( 	order_id VARCHAR(15) NOT NULL, 	order_date VARCHAR(15) NOT NULL, 	ship_date VARCHAR(15) NOT NULL, 	ship_mode VARCHAR(14) NOT NULL, 	customer_name VARCHAR(22) NOT NULL, 	segment VARCHAR(11) NOT NULL, 	state VARCHAR(36) NOT NULL, 	country VARCHAR(32) NOT NULL, 	market VARCHAR(6) NOT NULL, 	region VARCHAR(14) NOT NULL, 	product_id VARCHAR(16) NOT NULL, 	category VARCHAR(15) NOT NULL, 	sub_category VARCHAR(11) NOT NULL, 	product_name VARCHAR(127) NOT NULL, 	sales decimal(38, 3) NOT NULL, 	quantity DECIMAL(38, 0) NOT NULL, 	discount DECIMAL(38, 3) NOT NULL, 	profit DECIMAL(38, 8) NOT NULL, 	shipping_cost DECIMAL(38, 2) NOT NULL, 	order_priority VARCHAR(8) NOT NULL, 	`year` DECIMAL(38, 0) NOT NULL )')


# In[52]:


cursor.execute("show tables")


# In[53]:


cursor.fetchall()


# In[55]:


pwd


# In[57]:


cursor.execute('create table glass(col1 int, col2 float, col3 float, col4 float, col5 float, col6 float, col7 float, col8 float, col9 float, col10 float, col11 int)')


# In[82]:


import csv
with open("glass.data", "r") as f:
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        print(i)


# In[63]:


cursor.execute('insert into glass values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)')


# In[77]:


cursor.execute('select * from glass')


# In[78]:


cursor.fetchall()


# In[67]:


mydb.commit()


# In[76]:


import csv
with open("glass.data", "r") as f:
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        cursor.execute(f'insert into glass values({i[0]})')
mydb.commit()


# In[ ]:




