# coding: utf-8

"""
    alertmanager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.client_app_schema import ClientAppSchema  # noqa: E501
from openapi_client.rest import ApiException

class TestClientAppSchema(unittest.TestCase):
    """ClientAppSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClientAppSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientAppSchema`
        """
        model = openapi_client.models.client_app_schema.ClientAppSchema()  # noqa: E501
        if include_optional :
            return ClientAppSchema(
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '', 
                deleted = True, 
                contract = '', 
                labels = None, 
                id = '', 
                token = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                url = '', 
                billing_id = ''
            )
        else :
            return ClientAppSchema(
                id = '',
        )
        """

    def testClientAppSchema(self):
        """Test ClientAppSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
