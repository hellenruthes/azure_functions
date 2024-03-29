import azure.functions as func
import datetime
import json
import logging
import csv
import codecs

app = func.FunctionApp()

# Commenting out the existing code
"""
@app.function_name("FirstHTTPFunction")
@app.route(route="myroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("hellen's test")
    return func.HttpResponse("test worked",
        status_code = 200)
    

@app.function_name("SecondHTTPFunction")
@app.route(route="newroute", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("hellen's test")
    name = req.params.get('name')
    if name:
        message = f"Hello, {name}"
    else:
        message = "hello, no name"
    return func.HttpResponse(message, 
        status_code = 200)
    

@app.function_name("MyFirstBlobFunction")
@app.blob_trigger(arg_name="myblob",
                path="newcontainer/People.csv", connection="AzureWebJobsStorage")
def test_function(myblob: func.InputStream):
    logging.info("Blob trigger worked")
    logging.info(f"Blob name: {myblob.name}")
"""

@app.function_name("ReadFileBlobFunction")
@app.blob_trigger(arg_name="readfile",
                path="newcontainer/data.csv", 
                connection="AzureWebJobsStorage")
def test_function(readfile: func.InputStream):
    reader=csv.reader(codecs.iterdecode(readfile, 'utf-8'))
    for line in reader:
        logging.info(line)


   

@app.route(route="test_deploy", auth_level=func.AuthLevel.ANONYMOUS)
def test_deploy(req: func.HttpRequest) -> func.HttpResponse:
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