# Airflow Project based on Twtitter data

## Description
 Building basic and simple ETL pipeline using Airfow with Twitter data
The idea behind this project is to understand and implement basic functionalities of Airflow
Building Dags, Understanding what tasks, Task instance, pipelines is the motive behind taking up project.

## Concepts / Requirements

### Installing Airflow

The most time I spent on in this project is on installing Airflow software in my laptop. I tried to install in Amazon EC2 instance but was unable to do it.
Then I tried to install it in my windows system directly, but had multiple issues with dependencies not being there. It took couple of days to find what was happening and atlast was not able to install it directly into my system. 

Then I tried to install Airflow in an WSL instance. It worked and below are the steps to do it:
There are multiple ways to install WSL. I will mention how I did it:
 * First, Open Windows Powershell, then enter the following command  :  ``` wsl --install ```
 * Restart your computer if asked.
 * Then open the Ubuntu Environment and install the necessary packages:
    * ``` sudo apt-get update ```
    * ``` sudo apt-get install -y python3 python3-pip python3-venv ```
    * Then create a virtual environment to start the airflow installation process :
       * ``` python3 -m venv airflow_venv ```
       * ``` source airflow_venv/bin/activate ```
    * ``` export AIRFLOW_HOME=~/airflow ```
    * Install Airfow :
      
      ``` pip install apache-airflow[postgres,google] --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.8.txt" ```
    * Initialize Airflow DB : ``` airflow db init ```
    * Create an admin user to access Airflow WebUI and create/run dags
  
  ```      
  airflow users create \
  --username admin \
  --firstname FIRST_NAME \
  --lastname LAST_NAME \
  --role Admin \
  --email admin@example.com
 ```

   * Once the above command is run, a prompt to enter the password will be generated which can be used to login into Airflow WebUI
   * Start the Airflow web server : ``` airflow webserver --port 8080 ```
   * Access the web server : ``` http://localhost:8080 ```

### Creating DAG
   #### Create twitter_etl.py

 * It reads csv file from the local path ('/home/venkat/airflow/twitter_dag/cleandata.csv')
 * In order to move files from Windows to WSL Ubuntu instance, go to File explorer and type ``` \\wsl$ ``` to access the Ubuntu system and place the files in the required folder.
 * Some basic transformation logic is written and the updated file is returned ('/home/venkat/airflow/twitter_dag/elon_musk_tweets.csv').

   #### Create twitter_dag.py

 * Importing necessary packages and defining the default arguments for the DAG.
 * Create a instance for the DAG.
 * Define the tasks that DAG needs to run (run_etl).
 * I created a PythonOperator task since the transformation code (twitter_etl.py) is written using Python.
 * Call the Task instance to run.

 * If multiple tasks are created, you can use upstream or downstream symbols to call and run the tasks.
    * For Example : Consider there are two tasks in the DAG : run_etl and save_etl.
    * If save_etl needs to be run after run_etl, then you need to mention like this
      
      ``` run_etl >> save_etl ``` or ``` save_etl << run_etl ```
 * This is how a DAG is created.
 
 
 ### Executing DAG using Airflow Web Interface

 * It is very simple to execute DAG usign Airflow Web UI.
 * Once you enter into Web UI, we can search for our DAG in 'Search DAG' search box.
 * Select the required DAG. On the right corner you can see run button (somewhat similar to this --> :arrow_forward:), click it and select Run DAG.
 * It will execute the DAG. Go on to Graph mode in Web UI and if the box is surrouded by green border, it means the DAG run is successful.
 * 



   
