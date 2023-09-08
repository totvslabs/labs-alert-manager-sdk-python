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

from labs_alert_manager_client.models.policy_schema import PolicySchema  # noqa: E501

class TestPolicySchema(unittest.TestCase):
    """PolicySchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicySchema:
        """Test PolicySchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicySchema`
        """
        model = PolicySchema()  # noqa: E501
        if include_optional:
            return PolicySchema(
                channels = [
                    ''
                    ],
                client_source = '',
                client_uuid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted = True,
                enabled = True,
                filters = None,
                frequency = True,
                frequency_minutes = 56,
                frequency_occurrences = 56,
                id = '',
                name = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PolicySchema(
                channels = [
                    ''
                    ],
                client_source = '',
                client_uuid = '',
                deleted = True,
                enabled = True,
                filters = None,
                frequency = True,
                frequency_minutes = 56,
                frequency_occurrences = 56,
                id = '',
                name = '',
        )
        """

    def testPolicySchema(self):
        """Test PolicySchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
