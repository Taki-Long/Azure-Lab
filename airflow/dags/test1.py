from airflow.decorators import dag
from airflow.utils.dates import days_ago
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

@dag(dag_id="test", start_date=days_ago(2), schedule=None)
def generate_dag():
    action1 = SQLExecuteQueryOperator(
        task_id="action1",
        conn_id='test_mysql',
        sql='select * from test_table',
        database='test',
    )

    action2 = SimpleHttpOperator(
        task_id="action2",
        http_conn_id='test_http',
        method='POST',
        endpoint='api/hello',
        data='{"name": "{{ ti.xcom_pull(task_ids="action1")[0][0] }}"}',
    )

    action2.set_upstream(action1)

generate_dag()