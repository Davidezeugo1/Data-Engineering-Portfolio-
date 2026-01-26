# FROM python

# WORKDIR /first_project

# COPY . /first_project
# COPY /data /first_project



# # Install Python packages here
# RUN pip install pandas
# RUN pip install mysql-connector-python
# RUN pip install pymysql
# RUN pip install psycopg2
# RUN pip install sqlalchemy

# environment:
#     - POST_DATABASE_URL=postgresql+psycopg2://user:password@host.docker.internal:5432/mydb
#     - MYSQL_DATABASE_URL=mysql+pymysql://root:Davvysql#1@host.docker.internal:3306/sqldb 


# CMD ["bash", "-c", "python3 loadsqldb.py && python3 loadtopost.py && python3 truncate.py"] 
 
# Use an official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /first_project

# Copy your project files into the container
COPY . /first_project
# If you have a 'data' folder inside your project, use:
COPY data /first_project/data

# Install required Python packages in one layer
RUN pip install pandas
RUN pip install mysql-connector-python
RUN pip install pymysql
RUN pip install psycopg2-binary
RUN pip install sqlalchemy


# Run your Python scripts sequentially
CMD ["bash", "-c", "python3 loadsqldb.py && python3 loadtopost.py && sleep 150 && python3 truncate.py"] 