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
      name: str
      dag: str
      actions: 
        - name: action1
          type: LOAD_MY_SQL_DATA
          parameters: {dict}
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


CREATE TABLE test (name VARCHAR(20));