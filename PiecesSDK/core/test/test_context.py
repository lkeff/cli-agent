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

from openapi_client.models.context import Context  # noqa: E501

class TestContext(unittest.TestCase):
    """Context unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Context:
        """Test Context
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Context`
        """
        model = Context()  # noqa: E501
        if include_optional:
            return Context(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                os = '',
                application = openapi_client.models.application.Application(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    name = 'SUBLIME', 
                    version = '', 
                    platform = 'WEB', 
                    onboarded = True, 
                    privacy = 'OPEN', 
                    capabilities = 'LOCAL', 
                    mechanism = 'MANUAL', 
                    automatic_unload = True, ),
                health = openapi_client.models.health.Health(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    os = openapi_client.models.os_health.OSHealth(
                        id = '', 
                        version = '', ), ),
                user = openapi_client.models.user_profile.UserProfile(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    picture = 'https://picsum.photos/200', 
                    email = 'user@pieces.app', 
                    created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                    updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                        value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                    username = '', 
                    id = '', 
                    name = '', 
                    aesthetics = openapi_client.models.aesthetics.Aesthetics(
                        theme = openapi_client.models.theme.Theme(
                            dark = True, ), 
                        font = openapi_client.models.font.Font(
                            size = 56, ), ), 
                    vanityname = '', 
                    allocation = openapi_client.models.allocation_cloud.AllocationCloud(
                        id = '', 
                        user = '', 
                        urls = openapi_client.models.allocation_cloud_urls.AllocationCloudUrls(
                            base = openapi_client.models.allocation_cloud_url.AllocationCloudUrl(
                                status = 'PENDING', 
                                url = '', ), 
                            id = openapi_client.models.allocation_cloud_url.AllocationCloudUrl(
                                status = 'PENDING', 
                                url = '', ), 
                            vanity = , ), 
                        status = openapi_client.models.allocation_cloud_status.AllocationCloudStatus(
                            cloud = 'PENDING', ), 
                        project = '', 
                        version = '', 
                        region = '', ), 
                    providers = openapi_client.models.external_providers.ExternalProviders(
                        iterable = [
                            openapi_client.models.external_provider.ExternalProvider(
                                type = 'github', 
                                user_id = '', 
                                access_token = '', 
                                expires_in = 56, 
                                created = , 
                                updated = , 
                                profile_data = openapi_client.models.external_provider_profile_data.ExternalProviderProfileData(
                                    name = '', 
                                    picture = '', 
                                    nickname = '', 
                                    email = '', 
                                    email_verified = True, 
                                    node_id = '', 
                                    gravatar_id = '', 
                                    url = '', 
                                    html_url = '', 
                                    followers_url = '', 
                                    following_url = '', 
                                    gists_url = '', 
                                    starred_url = '', 
                                    subscriptions_url = '', 
                                    organizations_url = '', 
                                    repos_url = '', 
                                    events_url = '', 
                                    received_events_url = '', 
                                    site_admin = True, 
                                    company = '', 
                                    blog = '', 
                                    anchor = '', 
                                    hireable = True, 
                                    bio = '', 
                                    twitter_username = '', 
                                    public_repos = 56, 
                                    public_gists = 56, 
                                    followers = 56, 
                                    following = 56, 
                                    created_at = '', 
                                    updated_at = '', 
                                    private_gists = 56, 
                                    total_private_repos = 56, 
                                    owned_private_repos = 56, 
                                    disk_usage = 56, 
                                    collaborators = 56, 
                                    two_factor_authentication = True, ), 
                                connection = '', 
                                is_social = True, )
                            ], ), 
                    auth0 = openapi_client.models.auth0_user_metadata.Auth0UserMetadata(
                        global_id = '', 
                        cloud_key = '', 
                        stripe_customer_id = '', 
                        vanityname = '', ), )
            )
        else:
            return Context(
                os = '',
                application = openapi_client.models.application.Application(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    id = '', 
                    name = 'SUBLIME', 
                    version = '', 
                    platform = 'WEB', 
                    onboarded = True, 
                    privacy = 'OPEN', 
                    capabilities = 'LOCAL', 
                    mechanism = 'MANUAL', 
                    automatic_unload = True, ),
                health = openapi_client.models.health.Health(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    os = openapi_client.models.os_health.OSHealth(
                        id = '', 
                        version = '', ), ),
        )
        """

    def testContext(self):
        """Test Context"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
