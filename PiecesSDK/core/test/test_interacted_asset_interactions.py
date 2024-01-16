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

from openapi_client.models.interacted_asset_interactions import InteractedAssetInteractions  # noqa: E501

class TestInteractedAssetInteractions(unittest.TestCase):
    """InteractedAssetInteractions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InteractedAssetInteractions:
        """Test InteractedAssetInteractions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InteractedAssetInteractions`
        """
        model = InteractedAssetInteractions()  # noqa: E501
        if include_optional:
            return InteractedAssetInteractions(
                viewed = 'PY-M-DTh:m:s',
                touched = True,
                scrolled = True
            )
        else:
            return InteractedAssetInteractions(
                viewed = 'PY-M-DTh:m:s',
        )
        """

    def testInteractedAssetInteractions(self):
        """Test InteractedAssetInteractions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
