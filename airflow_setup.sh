#!/bin/bash
export AIRFLOW_HOME=$(pwd)
airflow version
source airflow_configure_evironment_variables.sh
airflow initdb