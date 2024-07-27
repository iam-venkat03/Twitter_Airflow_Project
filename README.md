# Airflow Project based on Twtitter data

## Description
This project involves building a basic ETL pipeline using Apache Airflow to process Twitter data. 
The primary objective is to gain a deeper understanding of Airflow's core functionalities, such as creating Directed Acyclic Graphs (DAGs), managing tasks, and executing pipelines.

## Concepts / Requirements

### Installing Airflow

A significant portion of this project was dedicated to setting up Apache Airflow on my laptop. After unsuccessful attempts to install it on an Amazon EC2 instance and directly on a Windows system, 
I encountered numerous dependency issues. Eventually, I successfully installed Airflow using the Windows Subsystem for Linux (WSL). 
Here are the steps I followed:

 1. Open Windows PowerShell and run the following command:
   
    ``` wsl --install ```

     * Restart your computer if asked.
   
 3. Set Up the Ubuntu Environment:
    Open the Ubuntu terminal and install the necessary packages
    
     ``` sudo apt-get update ```
    
     ``` sudo apt-get install -y python3 python3-pip python3-venv ```
    
 4. Create a virtual environment for the Airflow installation:

    ```
    python3 -m venv airflow_venv 
    source airflow_venv/bin/activate 
    export AIRFLOW_HOME=~/airflow
    ```
    
     * Install Airfow :
      
      ``` pip install apache-airflow[postgres,google] --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.8.txt" ```
    
       * Initialize the Airflow Database:
         
           ``` airflow db init ```
       
       * Create an admin user to access Airflow WebUI and create/run dags
  
  ```      
  airflow users create \
  --username admin \
  --firstname FIRST_NAME \
  --lastname LAST_NAME \
  --role Admin \
  --email admin@example.com
 ```

   * You will be prompted to set a password for the admin user, which will be used to log in to the Airflow Web UI.
     
   * Start the Airflow web server : ``` airflow webserver --port 8080 ```
     
   * Access the Airflow Web UI:
     * Navigate to ``` http://localhost:8080 ``` in your web browser.

### Creating DAG 
#### Create twitter_etl.py

* This script reads a CSV file from a specified path (/home/username/airflow/twitter_dag/cleandata.csv).
 
* To transfer files from Windows to the WSL Ubuntu environment, use the File Explorer and enter ``` \\wsl$ ``` to access the Ubuntu system. Place the files in the desired folder.
  
* Basic data transformation logic is applied, and the output file is saved as /home/username/airflow/twitter_dag/elon_musk_tweets.csv.

#### Create twitter_dag.py

* Import necessary packages and define default arguments for the DAG.
  
* Create a DAG instance.
  
* Define the tasks the DAG needs to execute (e.g., run_etl).
  
* Use a PythonOperator to run the transformation script (twitter_etl.py).
  
* Call the Task instance to run.
  
* Set task dependencies using upstream or downstream symbols

    * For Example : Consider there are two tasks in the DAG : run_etl and save_etl.
    * If save_etl needs to be run after run_etl, then you need to mention like this
      
      ``` run_etl >> save_etl ``` or ``` save_etl << run_etl ```
 
 ### Executing DAG using Airflow Web Interface

 * It is very simple to execute DAG usign Airflow Web UI.
   
 * To execute a DAG via the Airflow Web UI, search for the desired DAG using the "Search DAG" box.
   
 * Select the DAG and click the run button(somewhat similar to this --> :arrow_forward:) in the top right corner, then select "Run DAG".
   
 * The DAG execution status can be monitored in the Graph view; a green border indicates a successful run.

![Screenshot 2024-07-24 222926](https://github.com/user-attachments/assets/71b9ea10-ba98-4258-9327-2d068d440f4c)

 * You can see the runs and its status like this :
   
 ![Screenshot 2024-07-23 134104](https://github.com/user-attachments/assets/c8bcf4a1-8638-4965-968d-48c53653bd63)   

 ![Screenshot 2024-07-24 222843](https://github.com/user-attachments/assets/5242d09f-3a32-42bc-998e-03f5b0fecd74)

 * In this project, successful execution is verified by the presence of the elon_musk_tweets.csv file.
   
   * This is before DAG run :

       ![Screenshot 2024-07-23 133738](https://github.com/user-attachments/assets/fec31807-a49e-4f33-b966-adcd2d5b4178)

   * This is after DAG run:
  
       ![Screenshot 2024-07-24 223038](https://github.com/user-attachments/assets/d244f7f3-0f6f-483b-83cc-2962923a4eae)

   
 * The file is available and hence the DAG run is actually sucessful.

### Sidenote :
 #### Deleting a WSL Instance
 * To delete a WSL Instance, open Windows Powershell and type the following command:
   
   ```
   
   PS C:\Users\venka> wsl -l -v
   NAME      STATE           VERSION
   Ubuntu    Stopped         2
   PS C:\Users\venka> wsl --unregister Ubuntu
   Unregistering.
   The operation completed successfully.
   PS C:\Users\venka>
   
```
