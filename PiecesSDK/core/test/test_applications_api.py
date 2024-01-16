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

from openapi_client.api.applications_api import ApplicationsApi  # noqa: E501


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ApplicationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_applications_register(self) -> None:
        """Test case for applications_register

        /applications/register [POST]  # noqa: E501
        """
        pass

    def test_applications_session_close(self) -> None:
        """Test case for applications_session_close

        /applications/session/close [POST]  # noqa: E501
        """
        pass

    def test_applications_session_open(self) -> None:
        """Test case for applications_session_open

        /applications/session/open [POST]  # noqa: E501
        """
        pass

    def test_applications_session_snapshot(self) -> None:
        """Test case for applications_session_snapshot

        /applications/sessions/{session} [GET]  # noqa: E501
        """
        pass

    def test_applications_snapshot(self) -> None:
        """Test case for applications_snapshot

        /applications [GET]  # noqa: E501
        """
        pass

    def test_applications_specific_application_snapshot(self) -> None:
        """Test case for applications_specific_application_snapshot

        /applications/{application} [GET]  # noqa: E501
        """
        pass

    def test_applications_usage_engagement_interaction(self) -> None:
        """Test case for applications_usage_engagement_interaction

        /applications/usage/engagement/interaction [POST] Scoped to Apps  # noqa: E501
        """
        pass

    def test_applications_usage_engagement_keyboard(self) -> None:
        """Test case for applications_usage_engagement_keyboard

        /applications/usage/engagement/keyboard [POST] Scoped to Apps  # noqa: E501
        """
        pass

    def test_applications_usage_installation(self) -> None:
        """Test case for applications_usage_installation

        /applications/usage/installation [POST]  # noqa: E501
        """
        pass

    def test_post_applications_usage_updated(self) -> None:
        """Test case for post_applications_usage_updated

        /applications/usage/updated [POST]  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
