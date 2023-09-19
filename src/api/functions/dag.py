import jinja2

TEMPLATE = '''
from airflow.decorators import dag
from airflow.utils.dates import days_ago
{%- for action in actions %}
from {{ action.operator.package }} import {{ action.operator.class }}
{%- endfor %}

@dag(dag_id="{{ name }}", start_date=days_ago(2), schedule=None)
def generate_dag():
{%- for action in actions %}
    {{ action.name }} = {{ action.operator.class }}(
        task_id="{{ action.name }}",
        {%- for key, value in action.parameters.items() %}
        {{ key }}='{{ value }}',
        {%- endfor %}
    )
{% endfor %}
{%- for action in actions %}
    {%- for dep in action.dependences %}
    {{ action.name }}.set_upstream({{ dep }})
    {%- endfor %}
{%- endfor %}

generate_dag()
'''

def generate_dag(data):
    env = jinja2.Environment()
    template = env.from_string(TEMPLATE)
    dag = template.render(data)
    return dag