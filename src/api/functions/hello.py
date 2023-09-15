import logging
import json
import base64
import azure.functions as func 

blueprint = func.Blueprint() 

@blueprint.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS,)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    principal_raw = req.headers.get('x-ms-client-principal')
    if not principal_raw:
        return func.HttpResponse(
             "Unauthorized",
             status_code=401
        )
    principal_json = base64.b64decode(principal_raw).decode('utf-8')
    principal = json.loads(principal_json)

    if name:
        return func.HttpResponse(f"Hello, {principal['userDetails']}, you say {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"Hello, {principal['userDetails']}, you say nothing. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
