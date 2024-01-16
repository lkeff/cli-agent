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

from openapi_client.models.tracked_format_event_identifier_description_pairs import TrackedFormatEventIdentifierDescriptionPairs  # noqa: E501

class TestTrackedFormatEventIdentifierDescriptionPairs(unittest.TestCase):
    """TrackedFormatEventIdentifierDescriptionPairs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackedFormatEventIdentifierDescriptionPairs:
        """Test TrackedFormatEventIdentifierDescriptionPairs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackedFormatEventIdentifierDescriptionPairs`
        """
        model = TrackedFormatEventIdentifierDescriptionPairs()  # noqa: E501
        if include_optional:
            return TrackedFormatEventIdentifierDescriptionPairs(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                format_created = 'a_format_was_created',
                format_copied = 'if_a_format_was_entirely_copied',
                format_partially_copied = 'if_a_format_was_partially_copied',
                format_downloaded = 'if_a_format_was_downloaded',
                format_deleted = 'if_a_format_was_deleted',
                format_generic_classification_updated = 'if_a_generic_classification_was_changed_on_a_format',
                format_specific_classification_updated = 'if_a_specific_classification_was_changed_on_a_format',
                format_updated = 'a_format_was_updated',
                format_inserted = 'a_format_was_inserted',
                format_value_edited = 'a_format_value_was_edited'
            )
        else:
            return TrackedFormatEventIdentifierDescriptionPairs(
        )
        """

    def testTrackedFormatEventIdentifierDescriptionPairs(self):
        """Test TrackedFormatEventIdentifierDescriptionPairs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
