# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.tlp_directed_discovery_filters import TLPDirectedDiscoveryFilters  # noqa: E501

class TestTLPDirectedDiscoveryFilters(unittest.TestCase):
    """TLPDirectedDiscoveryFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TLPDirectedDiscoveryFilters:
        """Test TLPDirectedDiscoveryFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TLPDirectedDiscoveryFilters`
        """
        model = TLPDirectedDiscoveryFilters()  # noqa: E501
        if include_optional:
            return TLPDirectedDiscoveryFilters(
                iterable = [
                    openapi_client.models.tlp_directed_discovery_filter.TLPDirectedDiscoveryFilter(
                        name = 'FUNCTION', )
                    ]
            )
        else:
            return TLPDirectedDiscoveryFilters(
                iterable = [
                    openapi_client.models.tlp_directed_discovery_filter.TLPDirectedDiscoveryFilter(
                        name = 'FUNCTION', )
                    ],
        )
        """

    def testTLPDirectedDiscoveryFilters(self):
        """Test TLPDirectedDiscoveryFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
