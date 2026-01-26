
#install the needed driver
#python3 -m pip install psycopg2
#python3 -m pip install sqlalchemy
#python3 -m pip install pandas 

#import the libraries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import mysql.connector 
import logging 


#Creat logging for logs and data
logging.basicConfig(
    filename="logs.log",
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(message)s',
    filemode='a'
)

Datalog=logging.getLogger(__name__)
Datalog.propagate = False
Datalog.setLevel(logging.DEBUG) 
handler=logging.FileHandler('data.log', mode='a')
format=logging.Formatter ('%(asctime)s-%(levelname)s-%(message)s')
handler.setFormatter(format)
Datalog.addHandler(handler)

logging.debug('Logging started For LOADTOPOST.PY:')
Datalog.debug('Logging started For LOADTOPOST.PY:') 


#create the connection for both mysql and postgresql
conn = psycopg2.connect(
    host='host.docker.internal',
    database="postsqldb",
    user='postgres',
    password='Davvysql#1'
)

myconn= mysql.connector.connect( 
    user='root',
    password='Davvysql#1',
    host='host.docker.internal',
    database='sqldb',
    ssl_disabled=True
)

#create the cursor for Mysql and Postgresql
postcur = conn.cursor()
mycur = myconn.cursor()
postcur.execute('select version();')
mycur.execute('select version();')

#log the connection
logging.debug(f'Postgresql connection verision: {postcur.fetchall()}')
logging.debug(f'MySQL connection verision: {mycur.fetchall()}')

#create the sqlalchemy engine
engine = create_engine(f"postgresql+psycopg2://postgres:Davvysql#1@host.docker.internal:5432/postsqldb") 
logging.debug(f'sqlalchemy engine: {engine}') 

#create a connect engine
e = create_engine(f"mysql+pymysql://root:Davvysql#1@host.docker.internal/sqldb") 
logging.debug(f'sqlalchemy engine: {e}')


postcur.execute(" SELECT datname FROM pg_database;")
mycur.execute("show databases;")
Datalog.info(f'Show postgresql databases: {postcur.fetchall()}')
Datalog.info(f'Show Mysql databases: {mycur.fetchall()}') 


# second way to query the table to make a new dataframe
query = '''
    SELECT 
        category,
        country, 
        SUM(amount) AS sum_amount 
    FROM factsales AS F
    LEFT JOIN dimcategory AS dca ON F.categoryid = DCA.categoryid
    LEFT JOIN dimcountry AS dco ON F.countryid = dco.countryid
    GROUP BY category, country
    ORDER BY country, category;
'''

df2 = pd.read_sql_query(query, con=e)
logging.debug("First query was ran")
Datalog.info(f'New Dataframe: {df2.head(5)}') 


#Second Query for the new dataframe
query2='''select 
(amount) as Amountsum,
dd.date
from factsales as F left join dimdate as dd 
on F.dateid = dd.dateid;'''
df3 = pd.read_sql_query(query2, con=e)
logging.debug("Second query was ran")
Datalog.info(f'New Dataframe: {df3.head(5)}')


#Transfer the new dataframes into the postgresql database
df2.to_sql('amountsum', engine , if_exists='replace', index=False)
df3.to_sql('amounttime', engine,  if_exists='replace', index=False)

logging.debug("Dataframe 2 and 3 are moved to Postgresql database")
Datalog.info(f'NEW DATA IN POSTGRESQL: {df2}')
Datalog.info(f'NEW DATA IN POSTGRESQL: {df3}')

#close the connection 
mycur.close()
postcur.close()
logging.debug('Close both mycur and postcur.')

conn.close()
myconn.close()
logging.debug('Both MySQL and POSTGRESQL Connection closed')

