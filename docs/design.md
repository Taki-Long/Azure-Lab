1. UI
   1. Workflow 列表 -> List接口
      1. 创建 - 跳转编辑页面
      2. 编辑 - 跳转编辑页面
      3. 删除 - Delete接口
      4. 运行 - Run接口 (Run 页面)
   2. Workflow 编辑页面 -> Get接口(编辑时)
      1. React Flow
      2. 保存 -> Save接口

2. Backend
  - Models:
    - Workflow model:
      ```yaml
      id: str
      name: str
      dag: str
      parameter:
        - name: string
          type: file | string | number
      tasks: 
        - {task_name}:
          type: 
      ```
    - Run model:
      ```yaml

      ```
  - APIs:
    - Get /api/workflow/{name} *
      - Response: workflow model
    - Get /api/workflow
      - Response: list of workflow models
    - Post /api/workflow *
      - Body: workflow model
      - Response: workflow model details
      - Create Airflow DAG
    - Delete /api/workflow/{name}
    - Put /api/workflow/{name}
      - Body: workflow model 
    - Post /api/workflow/{name}/run
      - Response: run id
    - Get /api/workflow/{name}/run/{id}
      - Response: Run details

  - Database:
    - Azure Cosmos DB for MongoDB

  - Actions
    - Action Type: DataLoader | 
  
  - Data Provider
    - Type
      - RDBMS
    - Connection




/{name}/{run_id}/{task_id}/

1. Workflow User Inputs. 定义用户输入. 
   1. 文件
   2. 参数

2. 数据存放, 需要一个地方存放workflow 的结果或者中间过程.
   1. Azure Blob(S3) *
   2. DataFactory 大数据
   3. CosmosDB NoSQL
   4. PostgresSQL RDS
   

3. 每个tasks智能有1个的输入


## UI Workflow Definition:

```yaml
input:
  type: LOCAL_CSV_FILE
tasks:
  - task1:




```

