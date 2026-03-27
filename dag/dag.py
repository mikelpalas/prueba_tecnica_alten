from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import BaseOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

class TimeDiff(BaseOperator):
    def __init__(self, diff_date, **kwargs):
        super().__init__(**kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        now = datetime.now()
        diff = now - self.diff_date
        return str(diff)

with DAG(
    'test',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    tasks = [EmptyOperator(task_id=f'task_{n}') for n in range(1, 5)]
    impares = tasks[0::2]
    pares = tasks[1::2]

    impares >> pares

    diff_task = TimeDiff(
        task_id='time_diff_task',
        diff_date=datetime(2023, 1, 1)
    )

    start >> tasks >> end >> diff_task