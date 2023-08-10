# coding: utf-8

"""
    alertmanager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import labs_alert_manager_client
from labs_alert_manager_client.models.event_schema import EventSchema  # noqa: E501
from labs_alert_manager_client.rest import ApiException

class TestEventSchema(unittest.TestCase):
    """EventSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventSchema`
        """
        model = labs_alert_manager_client.models.event_schema.EventSchema()  # noqa: E501
        if include_optional :
            return EventSchema(
                client_source = '', 
                client_uuid = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                data = None, 
                event_type = '', 
                id = '', 
                labels = None, 
                schema_version = '', 
                severity = '', 
                status = '', 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return EventSchema(
                client_source = '',
                client_uuid = '',
                data = None,
                event_type = '',
                id = '',
                labels = None,
                schema_version = '',
                severity = '',
                status = '',
        )
        """

    def testEventSchema(self):
        """Test EventSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
