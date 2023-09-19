import logging
import json
import base64
import azure.functions as func 

blueprint = func.Blueprint() 

@blueprint.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS,)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(req.get_body().decode("utf-8"))

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
 
   
    if name:
        logging.info(f"Hello, you say {name}. This HTTP triggered function executed successfully.")
        return func.HttpResponse(f"Hello, you say {name}. This HTTP triggered function executed successfully.")
    else:
        logging.info(f"Hello, you say nothing. Pass a name in the query string or in the request body for a personalized response.")
        return func.HttpResponse(
             f"Hello, you say nothing. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
