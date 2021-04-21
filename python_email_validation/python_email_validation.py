from python_core import HttpEndpoint
from collections import namedtuple

class AbstractEmailValidation:
    api_key = None
    http_endpoint = HttpEndpoint(
        endpoint_subdomain='emailvalidation',
        global_req_params={
            'lang' : 'python'
        }
    )

    @staticmethod
    def configure(api_key):
        AbstractEmailValidation.api_key = api_key

    @staticmethod
    def verify(email):

        if AbstractEmailValidation.api_key is None:
            exception_type = "APINotConfiguredException"
            exception_msg = "Can't use the endpoint unless it's configured, use configure(api_key)"
            raise Exception(
                "[{}] : {}".format(exception_type, exception_msg)
            )

        try:
            req_params = {
                "api_key" : AbstractEmailValidation.api_key,
                "email" : email
            }
            response = AbstractEmailValidation.http_endpoint.get(
                req_params=req_params
            )
            # Convert the dict to an object
            for key in response:
                if (type(response[key]) == dict):
                    # dict holding only {value, text}
                    if "value" in response[key]:
                        response[key] = response[key]["value"]
                    # embedded dict, convert to object
                    else:
                        EmbeddedObject = namedtuple('EmbeddedObject', response[key])
                        embedded_obj = EmbeddedObject(**response[key])
                        response[key] = embedded_obj
            ResponseObject = namedtuple('ResponseObject', response.keys())
            response_obj = ResponseObject(**response)
            return response_obj

        except Exception as e:
            # HttpEndpoint has expressive exceptions
            raise SystemExit(e)