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

from openapi_client.models.qgpt_persons_related_output import QGPTPersonsRelatedOutput  # noqa: E501

class TestQGPTPersonsRelatedOutput(unittest.TestCase):
    """QGPTPersonsRelatedOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QGPTPersonsRelatedOutput:
        """Test QGPTPersonsRelatedOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QGPTPersonsRelatedOutput`
        """
        model = QGPTPersonsRelatedOutput()  # noqa: E501
        if include_optional:
            return QGPTPersonsRelatedOutput(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                persons = openapi_client.models.persons.Persons(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.person.Person(
                            id = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            type = openapi_client.models.person_type.PersonType(
                                basic = openapi_client.models.person_basic_type.PersonBasicType(
                                    username = '', 
                                    name = '', 
                                    picture = '', 
                                    email = '', 
                                    sourced = 'TWITTER', 
                                    url = '', 
                                    mailgun = openapi_client.models.mailgun_metadata.MailgunMetadata(
                                        message_id = '', ), ), 
                                platform = openapi_client.models.user_profile.UserProfile(
                                    picture = 'https://picsum.photos/200', 
                                    email = 'user@pieces.app', 
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
                                        vanityname = '', ), ), ), 
                            assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                                indices = {
                                    'key' : 56
                                    }, 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, 
                                    reference = 56, ), ), 
                            mechanisms = {
                                'key' : 'MANUAL'
                                }, 
                            interactions = 56, 
                            access = {
                                'key' : openapi_client.models.person_access.PersonAccess(
                                    scoped = 'OWNER', )
                                }, 
                            tags = openapi_client.models.flattened_tags.FlattenedTags(
                                iterable = [
                                    openapi_client.models.referenced_tag.ReferencedTag(
                                        id = '', 
                                        reference = openapi_client.models.flattened_tag.FlattenedTag(
                                            id = '', 
                                            text = '', 
                                            created = , 
                                            updated = , 
                                            category = 'HANDLE', 
                                            relationship = openapi_client.models.relationship.Relationship(
                                                id = '', 
                                                embeddings = openapi_client.models.embeddings.Embeddings(
                                                    iterable = [
                                                        openapi_client.models.embedding.Embedding(
                                                            raw = [
                                                                1.337
                                                                ], 
                                                            model = openapi_client.models.model.Model(
                                                                id = '', 
                                                                version = '', 
                                                                created = , 
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
                                                            created = , 
                                                            updated = , )
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
                                                updated = , ), 
                                            interactions = 56, 
                                            persons = openapi_client.models.flattened_persons.FlattenedPersons(
                                                iterable = [
                                                    openapi_client.models.referenced_person.ReferencedPerson(
                                                        id = '', )
                                                    ], ), ), )
                                    ], ), 
                            websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                iterable = [
                                    openapi_client.models.referenced_website.ReferencedWebsite(
                                        id = '', )
                                    ], ), 
                            models = {
                                'key' : openapi_client.models.person_model.PersonModel(
                                    asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                        id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                                    explanation = openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                        id = '', ), )
                                }, 
                            annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                iterable = [
                                    openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                        id = '', )
                                    ], ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
                explanations = {
                    'key' : ''
                    }
            )
        else:
            return QGPTPersonsRelatedOutput(
                persons = openapi_client.models.persons.Persons(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.person.Person(
                            id = '', 
                            created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                            deleted = , 
                            type = openapi_client.models.person_type.PersonType(
                                basic = openapi_client.models.person_basic_type.PersonBasicType(
                                    username = '', 
                                    name = '', 
                                    picture = '', 
                                    email = '', 
                                    sourced = 'TWITTER', 
                                    url = '', 
                                    mailgun = openapi_client.models.mailgun_metadata.MailgunMetadata(
                                        message_id = '', ), ), 
                                platform = openapi_client.models.user_profile.UserProfile(
                                    picture = 'https://picsum.photos/200', 
                                    email = 'user@pieces.app', 
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
                                        vanityname = '', ), ), ), 
                            assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                                indices = {
                                    'key' : 56
                                    }, 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, 
                                    reference = 56, ), ), 
                            mechanisms = {
                                'key' : 'MANUAL'
                                }, 
                            interactions = 56, 
                            access = {
                                'key' : openapi_client.models.person_access.PersonAccess(
                                    scoped = 'OWNER', )
                                }, 
                            tags = openapi_client.models.flattened_tags.FlattenedTags(
                                iterable = [
                                    openapi_client.models.referenced_tag.ReferencedTag(
                                        id = '', 
                                        reference = openapi_client.models.flattened_tag.FlattenedTag(
                                            id = '', 
                                            text = '', 
                                            created = , 
                                            updated = , 
                                            category = 'HANDLE', 
                                            relationship = openapi_client.models.relationship.Relationship(
                                                id = '', 
                                                embeddings = openapi_client.models.embeddings.Embeddings(
                                                    iterable = [
                                                        openapi_client.models.embedding.Embedding(
                                                            raw = [
                                                                1.337
                                                                ], 
                                                            model = openapi_client.models.model.Model(
                                                                id = '', 
                                                                version = '', 
                                                                created = , 
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
                                                            created = , 
                                                            updated = , )
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
                                                updated = , ), 
                                            interactions = 56, 
                                            persons = openapi_client.models.flattened_persons.FlattenedPersons(
                                                iterable = [
                                                    openapi_client.models.referenced_person.ReferencedPerson(
                                                        id = '', )
                                                    ], ), ), )
                                    ], ), 
                            websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                iterable = [
                                    openapi_client.models.referenced_website.ReferencedWebsite(
                                        id = '', )
                                    ], ), 
                            models = {
                                'key' : openapi_client.models.person_model.PersonModel(
                                    asset = openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                                        id = '2254f2c8-5797-40e8-ac56-41166dc0e159', ), 
                                    explanation = openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                        id = '', ), )
                                }, 
                            annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                iterable = [
                                    openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                        id = '', )
                                    ], ), 
                            score = openapi_client.models.score.Score(
                                manual = 56, 
                                automatic = 56, 
                                priority = 56, 
                                reuse = 56, 
                                update = 56, ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
        )
        """

    def testQGPTPersonsRelatedOutput(self):
        """Test QGPTPersonsRelatedOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
