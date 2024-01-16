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

from openapi_client.models.seeds import Seeds  # noqa: E501

class TestSeeds(unittest.TestCase):
    """Seeds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Seeds:
        """Test Seeds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Seeds`
        """
        model = Seeds()  # noqa: E501
        if include_optional:
            return Seeds(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                iterable = [
                    openapi_client.models.seed.Seed(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        asset = openapi_client.models.seeded_asset.SeededAsset(
                            metadata = openapi_client.models.seeded_asset_metadata.SeededAssetMetadata(
                                name = '', 
                                mechanism = 'MANUAL', 
                                tags = [
                                    openapi_client.models.seeded_asset_tag.SeededAssetTag(
                                        text = '', 
                                        category = 'HANDLE', )
                                    ], 
                                websites = [
                                    openapi_client.models.seeded_asset_website.SeededAssetWebsite(
                                        url = '', 
                                        name = '', )
                                    ], 
                                sensitives = [
                                    openapi_client.models.seeded_asset_sensitive.SeededAssetSensitive(
                                        text = '', 
                                        category = 'SECRET', 
                                        severity = 'LOW', 
                                        name = '', 
                                        description = '', )
                                    ], 
                                persons = [
                                    openapi_client.models.seeded_person.SeededPerson(
                                        access = openapi_client.models.person_access.PersonAccess(
                                            scoped = 'OWNER', 
                                            deleted = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                readable = 'Last week - June 3rd, 3:33 a.m.', ), ), 
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
                                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                                updated = , 
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
                                        model = openapi_client.models.person_model.PersonModel(
                                            explanation = openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                                id = '', 
                                                reference = openapi_client.models.flattened_annotation.FlattenedAnnotation(
                                                    id = '', 
                                                    created = , 
                                                    updated = , 
                                                    person = openapi_client.models.referenced_person.ReferencedPerson(
                                                        id = '', ), 
                                                    type = 'DESCRIPTION', 
                                                    text = '', 
                                                    pseudo = True, 
                                                    favorited = True, 
                                                    anchor = openapi_client.models.referenced_anchor.ReferencedAnchor(
                                                        id = '', ), 
                                                    conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                                        id = '', ), 
                                                    score = openapi_client.models.score.Score(
                                                        manual = 56, 
                                                        automatic = 56, 
                                                        priority = 56, 
                                                        reuse = 56, 
                                                        update = 56, ), 
                                                    messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                                                        iterable = [
                                                            openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                                                                id = '', )
                                                            ], 
                                                        indices = {
                                                            'key' : 56
                                                            }, ), ), ), ), 
                                        annotations = [
                                            openapi_client.models.seeded_annotation.SeededAnnotation(
                                                type = 'DESCRIPTION', 
                                                text = '', 
                                                pseudo = True, 
                                                favorited = True, )
                                            ], )
                                    ], 
                                annotations = [
                                    openapi_client.models.seeded_annotation.SeededAnnotation(
                                        type = , 
                                        text = '', 
                                        pseudo = True, 
                                        favorited = True, )
                                    ], 
                                hints = [
                                    openapi_client.models.seeded_hint.SeededHint(
                                        type = 'SUGGESTED_QUERY', 
                                        text = '', )
                                    ], 
                                anchors = [
                                    openapi_client.models.seeded_anchor.SeededAnchor(
                                        type = 'FILE', 
                                        watch = True, 
                                        fullpath = '', 
                                        name = '', )
                                    ], ), 
                            application = openapi_client.models.application.Application(
                                id = '', 
                                name = 'SUBLIME', 
                                version = '', 
                                platform = 'WEB', 
                                onboarded = True, 
                                privacy = 'OPEN', 
                                capabilities = 'LOCAL', 
                                automatic_unload = True, ), 
                            format = openapi_client.models.seeded_format.SeededFormat(
                                file = openapi_client.models.seeded_file.SeededFile(
                                    bytes = openapi_client.models.transferable_bytes.TransferableBytes(
                                        raw = [
                                            56
                                            ], 
                                        base64 = [
                                            56
                                            ], 
                                        base64_url = [
                                            56
                                            ], 
                                        data_url = [
                                            56
                                            ], ), 
                                    string = openapi_client.models.transferable_string.TransferableString(), ), 
                                fragment = openapi_client.models.seeded_fragment.SeededFragment(), 
                                classification = openapi_client.models.seeded_classification.SeededClassification(
                                    generic = 'CODE', 
                                    specific = 'csx', 
                                    rendering = 'HTML', ), ), 
                            discovered = True, 
                            available = openapi_client.models.available_formats.AvailableFormats(
                                iterable = [
                                    openapi_client.models.classification.Classification(
                                        generic = 'CODE', 
                                        specific = 'csx', )
                                    ], ), 
                            pseudo = True, ), 
                        type = 'SEEDED_ASSET', )
                    ]
            )
        else:
            return Seeds(
                iterable = [
                    openapi_client.models.seed.Seed(
                        schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                            migration = 56, 
                            semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                        asset = openapi_client.models.seeded_asset.SeededAsset(
                            metadata = openapi_client.models.seeded_asset_metadata.SeededAssetMetadata(
                                name = '', 
                                mechanism = 'MANUAL', 
                                tags = [
                                    openapi_client.models.seeded_asset_tag.SeededAssetTag(
                                        text = '', 
                                        category = 'HANDLE', )
                                    ], 
                                websites = [
                                    openapi_client.models.seeded_asset_website.SeededAssetWebsite(
                                        url = '', 
                                        name = '', )
                                    ], 
                                sensitives = [
                                    openapi_client.models.seeded_asset_sensitive.SeededAssetSensitive(
                                        text = '', 
                                        category = 'SECRET', 
                                        severity = 'LOW', 
                                        name = '', 
                                        description = '', )
                                    ], 
                                persons = [
                                    openapi_client.models.seeded_person.SeededPerson(
                                        access = openapi_client.models.person_access.PersonAccess(
                                            scoped = 'OWNER', 
                                            deleted = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                readable = 'Last week - June 3rd, 3:33 a.m.', ), ), 
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
                                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                                updated = , 
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
                                        model = openapi_client.models.person_model.PersonModel(
                                            explanation = openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                                id = '', 
                                                reference = openapi_client.models.flattened_annotation.FlattenedAnnotation(
                                                    id = '', 
                                                    created = , 
                                                    updated = , 
                                                    person = openapi_client.models.referenced_person.ReferencedPerson(
                                                        id = '', ), 
                                                    type = 'DESCRIPTION', 
                                                    text = '', 
                                                    pseudo = True, 
                                                    favorited = True, 
                                                    anchor = openapi_client.models.referenced_anchor.ReferencedAnchor(
                                                        id = '', ), 
                                                    conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                                        id = '', ), 
                                                    score = openapi_client.models.score.Score(
                                                        manual = 56, 
                                                        automatic = 56, 
                                                        priority = 56, 
                                                        reuse = 56, 
                                                        update = 56, ), 
                                                    messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                                                        iterable = [
                                                            openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                                                                id = '', )
                                                            ], 
                                                        indices = {
                                                            'key' : 56
                                                            }, ), ), ), ), 
                                        annotations = [
                                            openapi_client.models.seeded_annotation.SeededAnnotation(
                                                type = 'DESCRIPTION', 
                                                text = '', 
                                                pseudo = True, 
                                                favorited = True, )
                                            ], )
                                    ], 
                                annotations = [
                                    openapi_client.models.seeded_annotation.SeededAnnotation(
                                        type = , 
                                        text = '', 
                                        pseudo = True, 
                                        favorited = True, )
                                    ], 
                                hints = [
                                    openapi_client.models.seeded_hint.SeededHint(
                                        type = 'SUGGESTED_QUERY', 
                                        text = '', )
                                    ], 
                                anchors = [
                                    openapi_client.models.seeded_anchor.SeededAnchor(
                                        type = 'FILE', 
                                        watch = True, 
                                        fullpath = '', 
                                        name = '', )
                                    ], ), 
                            application = openapi_client.models.application.Application(
                                id = '', 
                                name = 'SUBLIME', 
                                version = '', 
                                platform = 'WEB', 
                                onboarded = True, 
                                privacy = 'OPEN', 
                                capabilities = 'LOCAL', 
                                automatic_unload = True, ), 
                            format = openapi_client.models.seeded_format.SeededFormat(
                                file = openapi_client.models.seeded_file.SeededFile(
                                    bytes = openapi_client.models.transferable_bytes.TransferableBytes(
                                        raw = [
                                            56
                                            ], 
                                        base64 = [
                                            56
                                            ], 
                                        base64_url = [
                                            56
                                            ], 
                                        data_url = [
                                            56
                                            ], ), 
                                    string = openapi_client.models.transferable_string.TransferableString(), ), 
                                fragment = openapi_client.models.seeded_fragment.SeededFragment(), 
                                classification = openapi_client.models.seeded_classification.SeededClassification(
                                    generic = 'CODE', 
                                    specific = 'csx', 
                                    rendering = 'HTML', ), ), 
                            discovered = True, 
                            available = openapi_client.models.available_formats.AvailableFormats(
                                iterable = [
                                    openapi_client.models.classification.Classification(
                                        generic = 'CODE', 
                                        specific = 'csx', )
                                    ], ), 
                            pseudo = True, ), 
                        type = 'SEEDED_ASSET', )
                    ],
        )
        """

    def testSeeds(self):
        """Test Seeds"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
