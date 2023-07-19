# from datetime import timedelta
# from check_if_update_csvs import check_if_update_csvs
# from update_csvs import update_csvs
# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator, ShortCircuitOperator
# from airflow.utils.dates import days_ago


# # Define the DAG's default arguments and schedule interval
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': days_ago(1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# with DAG(
#     'update_dash_data',
#     default_args=default_args,
#     description='Check if there has been an update in the db in the last 30 minutes, if so, update the csvs for dash to display',
#     schedule_interval=timedelta(minutes=30),
#     catchup=False,
# ) as dag:

#     # Use ShortCircuitOperator to control the flow based on the result of task1
#     task1_check = ShortCircuitOperator(
#         task_id='check_if_update_csvs',
#         python_callable= check_if_update_csvs,
#     )



#     # Task 2: Run the second function if the first function returned True
#     task2 = PythonOperator(
#         task_id='update_csvs',
#         python_callable=update_csvs,
#     )

    
#     task1_check >>  task2
