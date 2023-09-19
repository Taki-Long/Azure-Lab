import jinja2

data = {
    "name": "test",
    "actions": [
        {
            "name": "action1",
            "operator": {
                "package": "airflow.providers.common.sql.operators.sql",
                "class": "SQLExecuteQueryOperator",
            },
            "parameters": {
                "conn_id": "test_mysql",
                "sql": "select * from test_table",
                "database": "test",
            },
        },
        {
            "name": "action2",
            "operator": {
                "package": "airflow.providers.http.operators.http",
                "class": "SimpleHttpOperator",
            },
            "parameters": {
                "http_conn_id": "test_http",
                "method": "POST",
                "endpoint": "api/hello",
                "data": '{"name": "{{ ti.xcom_pull(task_ids="action1")[0][0] }}"}',
            },
            "dependences": ["action1"],
        },
    ],
}

# loader = jinja2.FileSystemLoader(
#     searchpath="/Users/taki/Projects/Azure-Lab/src/api/functions/"
# )
# env = jinja2.Environment(loader=loader)
# template = env.get_template("template.j2")
# outputText = template.render(data)
# print(outputText)

import json
print(json.dumps(data))