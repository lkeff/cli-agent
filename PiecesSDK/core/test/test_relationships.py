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

from openapi_client.models.relationships import Relationships  # noqa: E501

class TestRelationships(unittest.TestCase):
    """Relationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Relationships:
        """Test Relationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Relationships`
        """
        model = Relationships()  # noqa: E501
        if include_optional:
            return Relationships(
                iterable = [
                    openapi_client.models.relationship.Relationship(
                        id = '', 
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        embeddings = openapi_client.models.embeddings.Embeddings(
                            iterable = [
                                openapi_client.models.embedding.Embedding(
                                    raw = [
                                        1.337
                                        ], 
                                    model = openapi_client.models.model.Model(
                                        id = '', 
                                        version = '', 
                                        created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                            value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                        name = '', 
                                        description = '', 
                                        cloud = True, 
                                        type = 'BALANCED', 
                                        usage = 'OCR', 
                                        bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        quantization = '', 
                                        foundation = 'GPT_3.5', 
                                        downloaded = True, 
                                        loaded = True, 
                                        unique = '', 
                                        parameters = 1.337, 
                                        provider = 'APPLE', 
                                        cpu = True, 
                                        downloading = True, ), 
                                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                    updated = , 
                                    deleted = , )
                                ], ), 
                        edges = openapi_client.models.edges.Edges(
                            iterable = [
                                openapi_client.models.node.Node(
                                    id = '', 
                                    type = 'TAG', 
                                    root = True, 
                                    created = , )
                                ], ), 
                        created = , 
                        updated = , 
                        deleted = , )
                    ]
            )
        else:
            return Relationships(
                iterable = [
                    openapi_client.models.relationship.Relationship(
                        id = '', 
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        embeddings = openapi_client.models.embeddings.Embeddings(
                            iterable = [
                                openapi_client.models.embedding.Embedding(
                                    raw = [
                                        1.337
                                        ], 
                                    model = openapi_client.models.model.Model(
                                        id = '', 
                                        version = '', 
                                        created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                            value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                        name = '', 
                                        description = '', 
                                        cloud = True, 
                                        type = 'BALANCED', 
                                        usage = 'OCR', 
                                        bytes = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        ram = openapi_client.models.byte_descriptor.ByteDescriptor(
                                            value = 33600, 
                                            readable = '33.6 KB', ), 
                                        quantization = '', 
                                        foundation = 'GPT_3.5', 
                                        downloaded = True, 
                                        loaded = True, 
                                        unique = '', 
                                        parameters = 1.337, 
                                        provider = 'APPLE', 
                                        cpu = True, 
                                        downloading = True, ), 
                                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                    updated = , 
                                    deleted = , )
                                ], ), 
                        edges = openapi_client.models.edges.Edges(
                            iterable = [
                                openapi_client.models.node.Node(
                                    id = '', 
                                    type = 'TAG', 
                                    root = True, 
                                    created = , )
                                ], ), 
                        created = , 
                        updated = , 
                        deleted = , )
                    ],
        )
        """

    def testRelationships(self):
        """Test Relationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
