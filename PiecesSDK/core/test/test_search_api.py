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

from openapi_client.api.search_api import SearchApi  # noqa: E501


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_full_text_search(self) -> None:
        """Test case for full_text_search

        /search/full_text [GET]  # noqa: E501
        """
        pass

    def test_neural_code_search(self) -> None:
        """Test case for neural_code_search

        /search/neural_code [GET]  # noqa: E501
        """
        pass

    def test_tag_based_search(self) -> None:
        """Test case for tag_based_search

        /search/tag_based [POST]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
