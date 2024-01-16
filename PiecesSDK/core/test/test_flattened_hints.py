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

from openapi_client.models.flattened_hints import FlattenedHints  # noqa: E501

class TestFlattenedHints(unittest.TestCase):
    """FlattenedHints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlattenedHints:
        """Test FlattenedHints
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlattenedHints`
        """
        model = FlattenedHints()  # noqa: E501
        if include_optional:
            return FlattenedHints(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                iterable = [
                    openapi_client.models.referenced_hint.ReferencedHint(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        id = '', 
                        reference = openapi_client.models.flattened_hint.FlattenedHint(
                            id = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            mechanism = 'MANUAL', 
                            asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                            type = 'SUGGESTED_QUERY', 
                            text = '', 
                            model = openapi_client.models.referenced_model.ReferencedModel(
                                id = '', ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), ), )
                    ],
                indices = {
                    'key' : 56
                    },
                score = openapi_client.models.score.Score(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    manual = 56, 
                    automatic = 56, 
                    priority = 56, 
                    reuse = 56, 
                    update = 56, 
                    reference = 56, )
            )
        else:
            return FlattenedHints(
                iterable = [
                    openapi_client.models.referenced_hint.ReferencedHint(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        id = '', 
                        reference = openapi_client.models.flattened_hint.FlattenedHint(
                            id = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            mechanism = 'MANUAL', 
                            asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                            type = 'SUGGESTED_QUERY', 
                            text = '', 
                            model = openapi_client.models.referenced_model.ReferencedModel(
                                id = '', ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), ), )
                    ],
        )
        """

    def testFlattenedHints(self):
        """Test FlattenedHints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
