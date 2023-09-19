import json
import logging
import azure.functions as func

from mongoengine import Document, DictField, ListField, StringField, connect
from mongoengine.fields import ReferenceField

from functions.dag import generate_dag


class Action(Document):
    name = StringField()
    type = StringField()
    parameters = DictField()
    dependencies = ListField(StringField())


class Workflow(Document):
    name = StringField(primary_key=True)
    actions = ListField(ReferenceField(Action))
    meta = {"collection": "workflow"}


blueprint = func.Blueprint()

connect(host="mongodb://127.0.0.1:27017/hackathon")


@blueprint.route(
    route="workflow",
    methods=[func.HttpMethod.POST],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def create(req: func.HttpRequest) -> func.HttpResponse:
    data = req.get_body()
    logging.info(data.decode("utf-8"))
    wf = Workflow.from_json(data.decode("utf-8"), created=True)
    wf.save()
    dag = generate_dag(json.loads(data.decode("utf-8")))

    return func.HttpResponse(dag, status_code=200)


@blueprint.route(
    route="workflow/{name}",
    methods=[func.HttpMethod.GET],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def get(req: func.HttpRequest) -> func.HttpResponse:
    name = req.route_params["name"]
    wf = Workflow.objects.get(name=name)
    return func.HttpResponse(wf.to_json(), status_code=200)


@blueprint.route(
    route="workflow",
    methods=[func.HttpMethod.GET],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def list(req: func.HttpRequest) -> func.HttpResponse:
    wf_list = Workflow.objects
    return func.HttpResponse(wf_list.to_json(), status_code=200)


@blueprint.route(
    route="workflow/{name}",
    methods=[func.HttpMethod.DELETE],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def delete(req: func.HttpRequest) -> func.HttpResponse:
    name = req.route_params["name"]
    wf = Workflow.objects.get(name=name)
    wf.delete()
    return func.HttpResponse(status_code=200)
