import azure.functions as func
import functions.hello

app = func.FunctionApp() 

app.register_functions(functions.hello.blueprint) 



