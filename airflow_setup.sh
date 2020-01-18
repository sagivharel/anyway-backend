#!/bin/bash
export AIRFLOW_HOME=$(pwd)/processing_pipeline
airflow version
source airflow_configure_evironment_variables.sh
airflow initdb