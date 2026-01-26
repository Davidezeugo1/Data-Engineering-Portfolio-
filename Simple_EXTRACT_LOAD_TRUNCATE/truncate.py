
#import libraries 
import pandas as pd
import mysql.connector 
import psycopg2 
from sqlalchemy import create_engine   
import logging 

#Creat logging for logs and data
logging.basicConfig(
    filename= "logs.log", 
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

#Start logging 
logging.debug('LOGGING TRUNCATE.PY:') 
Datalog.debug('LOGGING TRUNCATE.PY:')  

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

#create the sqlalchemy engine
engine = create_engine(f"postgresql+psycopg2://postgres:Davvysql#1@host.docker.internal:5432/postsqldb") 
logging.debug(f'sqlalchemy engine: {engine}') 

#create a connect engine
e = create_engine(f"mysql+pymysql://root:Davvysql#1@host.docker.internal/sqldb") 
logging.debug(f'sqlalchemy engine: {e}')

query= '''SELECT 'dimcategory' AS table_name, COUNT(*) AS total FROM dimcategory
UNION ALL
SELECT 'factsales', COUNT(*) FROM factsales
UNION ALL
SELECT 'dimdate', COUNT(*) FROM dimdate
UNION ALL
SELECT 'dimcountry', COUNT(*) FROM dimcountry;'''
sqlcount=pd.read_sql(query, con=e)
Datalog.info(f'The rowcounts in MYSQL tables before TRUNCATE: {sqlcount}')

query2='''SELECT count(*) as postgrerowcount from amountsum, amounttime;'''
postcount=pd.read_sql(query2, con=engine)
Datalog.info(f'The rowcounts in POSTGRESQL tables before TRUNCATE: {postcount}')

#execute the truncate for both database 
mycur.execute("TRUNCATE TABLE dimcountry;TRUNCATE TABLE dimcategory;TRUNCATE TABLE dimdate;TRUNCATE TABLE factsales;") 

postcur.execute('TRUNCATE TABLE amountsum;')
postcur.execute('TRUNCATE TABLE amounttime;')
conn.commit()

logging.debug('Truncate command ran for both MYSQL and POSTGRESQL tables')


#query the turncated tables from both database
query= '''select count(*) as mysqlrowcount from dimcategory,factsales,dimdate, dimcountry;'''
sqlcount=pd.read_sql(query, con=e)
Datalog.info(f'The rowcounts in MYSQL tables after TRUNCATE: {sqlcount}') 

query2='''SELECT count(*) as postgrerowcount from amountsum, amounttime;'''
postcount=pd.read_sql(query2, con=engine)
Datalog.info(f'The rowcounts in POSTGRESQL tables after TRUNCATE: {postcount}')

logging.debug('Query count of rows in tables for MYSQL and POSTGRESQL')