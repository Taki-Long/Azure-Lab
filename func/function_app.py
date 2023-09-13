import azure.functions as func
import logging
import datetime

from azure.storage.blob import BlobSasPermissions, generate_blob_sas

app = func.FunctionApp()

@app.route(route="sas", auth_level=func.AuthLevel.ANONYMOUS)
def sas(req: func.HttpRequest) -> func.HttpResponse:
    
    start_time = datetime.datetime.now(datetime.timezone.utc)
    expiry_time = start_time + datetime.timedelta(days=1)

    sas_token = generate_blob_sas(
        account_name='azurelabinfralvmzi',
        container_name='test',
        blob_name='hello',
        account_key='4/rIY0D89YUouCfJj65jQpBB6Ee4RB6eMEawgpipwHuYD1Iy5+LaI6InXnx8txZjYugW4Qk9VaY4+AStc0z74Q==',
        permission=BlobSasPermissions(read=True,write=True),
        expiry=expiry_time,
        start=start_time
    )
    
    return func.HttpResponse(sas_token)



@app.route(route="HttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )