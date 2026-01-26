
#install the needed libaires 
#python3 -m pip install pandas
#python3 -m pip install mysql-connector-python
#python3 -m pip install pymysql

#import the needed APIS
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
import logging


#create logging Config
logging.basicConfig(filename="logs.log",
                    level=logging.DEBUG,
                    format= '%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')


Datalog=logging.getLogger(__name__)
Datalog.propagate = False
Datalog.setLevel(logging.DEBUG) 
handler=logging.FileHandler('data.log', mode='w',)
formatter= logging.Formatter( '%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
Datalog.addHandler(handler) 


logging.info("LOGGING FILE CREATED") 
Datalog.info("DATALOG FILE CREATED")

#create the mysql connection 
conn= mysql.connector.connect( 
    user='root',
    password='Davvysql#1',
    host='host.docker.internal',
    database='sqldb',
    ssl_disabled=True
)

#create a connect engine
e = create_engine(f"mysql+pymysql://root:Davvysql#1@host.docker.internal/sqldb") 
logging.debug(f"create a sqlalchmey connection:, {e}" )

#log the connection 
logging.info(f"Connected using mysql.connector:, {conn}") 

#create the cursor and show the databases in the MYSQL
cursor = conn.cursor() 
cursor.execute("SHOW DATABASES;")

#Logging
logging.debug('cursor.execute(SHOW DATABASES;)')
Datalog.debug(f"Databases:, {cursor.fetchall()}")

#connect into the sqldb database
cursor.execute("use sqldb;")
logging.debug('cursor.execute(use sqldb)') 

#check the tables in sqldb database
cursor.execute('show tables')
logging.debug('cursor.execute(show tables;)')
Datalog.debug(f"Tabels in SQLdb:, {cursor.fetchall()}")


#Read the CSV files with pd.read_csv
dimcatedata=pd.read_csv(f'/first_project/data/DimCategory.csv',  index_col=False) 
dimcountrydata=pd.read_csv(f'/first_project/data/DimCountry.csv',  index_col=False) 
dimdatedata=pd.read_csv(f'/first_project/data/DimData.csv',  index_col=False) 
factsalesdata =pd.read_csv(f'/first_project/data/FactSales.csv',  index_col=False) 
logging.debug("converting csv files converted to df")

# write the csv files into the Mysql database
dimcatedata.to_sql('dimcategory', con=e , if_exists='replace', index=False) 
dimcountrydata.to_sql('dimcountry', con=e , if_exists='replace', index=False) 
dimdatedata.to_sql('dimdate', con=e , if_exists='replace', index=False) 
factsalesdata.to_sql('factsales', con=e , if_exists='replace', index=False) 


#check thesqlbd database that the data was uploaded
df_check = pd.read_sql("SELECT * FROM DimCategory LIMIT 5;", con=e)
logging.debug("SELECT * FROM DimCategory LIMIT 5;")
Datalog.info(f"Preview of DimCategory:{df_check}")


df_check2 = pd.read_sql("SELECT * FROM DimCountry LIMIT 5;", con=e)
logging.debug("SELECT * FROM DimCountry LIMIT 5;")
Datalog.info(f"Preview of DimCountry:{df_check2}")


df_check3 = pd.read_sql("SELECT * FROM Dimdate LIMIT 5;", con=e)
logging.debug("SELECT * FROM Dimdate LIMIT 5;")
Datalog.info(f"Preview of Dimdate:{df_check3}")


df_check4 = pd.read_sql("SELECT * FROM Factsales LIMIT 5;", con=e)
logging.debug("SELECT * FROM Factsales LIMIT 5;")
Datalog.info(f"Preview of Factsales:{df_check4}")


#close the connection 
cursor.close()
logging.debug('Cursor closed')

conn.close()    
logging.debug('Connection closed')