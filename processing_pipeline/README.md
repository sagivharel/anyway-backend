# AirFlow Processing Pipeline:
### Important notes
- airflow sees the processing_pipeline folder as root so you also need to mark the "processing_pipeline" folder as a source root folder.
(If you are using pycharm: go to the Settings -> Project -> Project Structure -> click on the "processing_pipeline" folder and mark it as source)

### Folder structure:
The 'processing_pipeline' folder structure is as follows:   
    
##### Files:
- anyway_processing.py : the main python file which contains the airflow DAG object which controls the pipeline
- data_source_fetching.py : contains functions to get the raw data from the Drive / Bucket  
- utils.py : contains util functions like data loading
- constants.py :  contains constants
- pipeline_configuration.yaml : contains some key configurations for the pipeline like the data date string
- processing_example.py : an example -> can be ignored

##### Folders:
- cleaning, mapping, transformation, validation: folders which should contain python functions
- csv_files: folder which contains the raw and processed data csv files (created in the python file process if not exists)

-----------------------
### AirFlow setup
If it's the first time you run AirFlow:
Setup the Airflow env by running in your terminal (in the projects' folder):  `bash airflow_setup.sh`

### Use AirFlow
After setting up the AirFlow env
please open 2 terminal windows (in the projects' folder) and run these commands (each in a separate terminal window):
- `bash airflow_webserver.sh` - will start the AirFlow UI (go to http://localhost:8080/admin/)
- `bash airflow_scheduler.sh` - will start the scheduler, now you will be able to run your jobs


### Conventions:
- Where the Operator has `provide_context=True` argument the equivalent task function has to get `**context` as argument
- task_id should be the same as your variable name

-----------------------

# TODOs
- Get all the data from the Drive / Google's bucket
- Change the DB to be PostgreSQL
- Multiprocessing
- Save to DB whe finished
- Use the config file to find on which file to run 

-----------------------

### useful links:
- http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/
- https://airflow.apache.org/docs/stable/best-practices.html