# AirFlow Processing Pipeline:
### Important notes
- airflow sees the dags folder as root so you also need to mark the "dags" folder as a source root folder.
(If you are using pycharm:
    go to the Settings -> Project -> Project Structure -> click on the 'dags' folder and mark it as source)

### Folder structure:
The 'dags' folder structure is as follows:   
    
##### Files:
- anyway_processing.py : the main python file which contains the airflow DAG object which controls the pipeline
- data_source_fetching.py : contains functions to get the raw data from the Drive / Bucket  
- utils.py : contains util functions like data loading

##### Folders:

- cleaning: please put all the python functions which relate to cleaning the data
- mapping: please put all the python functions which relate to cleaning the data
- transformation: please put all the python functions which relate to transforming the data (making new columns, aggregating  etc)
- validation: please put all the python functions which relate to  the data
- csv_files: contain the raw and processed data csv files (created in the python file process if not exists)

-----------------------
### AirFlow setup
- run `export AIRFLOW_HOME=`pwd`/processing_pipeline` in your terminal (in the projects' folder)
- run `airflow version`
- run `airflow initdb` # TODO: change this to work with postgresql


### AirFlow UI
- In airflow.cfg change `load_examples = True` to `load_examples = False`
- run `airflow webserver` in your terminal (in the projects' folder)
- Go to http://localhost:8080/admin/


### AirFlow Run:
- run `export AIRFLOW_HOME=`pwd`/processing_pipeline` in your terminal (in the projects' folder)
- run `airflow scheduler`


### Conventions:

- task_id is written like this: `[module_name]__[function_name]`


# TODOs
- Get all the data from the Drive / Google's bucket
- Change the DB to be PostgreSQL