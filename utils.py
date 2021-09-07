from flask_apispec.views import MethodResource
from flask_restful import Resource


# pylint: disable=E0102
class Resource(MethodResource, Resource):
    pass