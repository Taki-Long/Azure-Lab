import azure.functions as func
import functions.workflow
import functions.hello

app = func.FunctionApp() 

app.register_functions(functions.workflow.blueprint) 
app.register_functions(functions.hello.blueprint) 
