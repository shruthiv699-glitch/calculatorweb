import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger processed a request.')
    return func.HttpResponse("Hello Elasticity!", status_code=200)
