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

from openapi_client.models.qgpt_relevance_input import QGPTRelevanceInput  # noqa: E501

class TestQGPTRelevanceInput(unittest.TestCase):
    """QGPTRelevanceInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QGPTRelevanceInput:
        """Test QGPTRelevanceInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QGPTRelevanceInput`
        """
        model = QGPTRelevanceInput()  # noqa: E501
        if include_optional:
            return QGPTRelevanceInput(
                var_schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                    migration = 56, 
                    semantic = 'MAJOR_0_MINOR_0_PATCH_1', ),
                query = '',
                paths = [
                    ''
                    ],
                seeds = openapi_client.models.seeds.Seeds(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.seed.Seed(
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
                        ], ),
                assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_asset_[dag_safety].ReferencedAsset [DAG Safety](
                            id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                            reference = openapi_client.models.flattened_asset_[dag_safety].FlattenedAsset [DAG Safety](
                                id = '2254f2c8-5797-40e8-ac56-41166dc0e159', 
                                name = '', 
                                creator = '497f6eca-6276-4993-bfeb-53cbbbba6f08', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                synced = , 
                                deleted = , 
                                formats = openapi_client.models.flattened_formats.FlattenedFormats(
                                    iterable = [
                                        openapi_client.models.referenced_format_[dag_safety].ReferencedFormat [DAG Safety](
                                            id = '102ff265-fdfb-4142-8d94-4932d400199c', )
                                        ], ), 
                                preview = openapi_client.models.flattened_preview.FlattenedPreview(
                                    base = '', 
                                    overlay = '', ), 
                                original = '0872ccbf-1d8f-4f46-9028-469794d72761', 
                                shares = openapi_client.models.flattened_shares_[dag_safe].FlattenedShares [DAG Safe](
                                    iterable = [
                                        openapi_client.models.flattened_share_[dag_safe].FlattenedShare [DAG SAFE](
                                            id = '', 
                                            asset = '', 
                                            user = '', 
                                            link = '', 
                                            access = 'PUBLIC', 
                                            accessors = openapi_client.models.accessors.Accessors(
                                                iterable = [
                                                    openapi_client.models.accessor.Accessor(
                                                        id = '', 
                                                        os = '', 
                                                        share = '', 
                                                        count = 56, 
                                                        user = openapi_client.models.flattened_user_profile.FlattenedUserProfile(
                                                            id = '', 
                                                            email = '', 
                                                            name = '', 
                                                            username = '', 
                                                            picture = '', 
                                                            vanityname = '', ), )
                                                    ], ), 
                                            created = , 
                                            short = '', 
                                            name = '', 
                                            assets = openapi_client.models.flattened_assets_[dag_safety].FlattenedAssets [DAG Safety](
                                                indices = {
                                                    'key' : 56
                                                    }, 
                                                score = openapi_client.models.score.Score(
                                                    manual = 56, 
                                                    automatic = 56, 
                                                    priority = 56, 
                                                    reuse = 56, 
                                                    update = 56, ), ), 
                                            distributions = openapi_client.models.flattened_distributions.FlattenedDistributions(
                                                iterable = [
                                                    openapi_client.models.referenced_distribution.ReferencedDistribution(
                                                        id = '', )
                                                    ], ), 
                                            score = openapi_client.models.score.Score(
                                                manual = 56, 
                                                automatic = 56, 
                                                priority = 56, 
                                                reuse = 56, 
                                                update = 56, ), )
                                        ], 
                                    score = , ), 
                                mechanism = 'MANUAL', 
                                websites = openapi_client.models.flattened_websites.FlattenedWebsites(
                                    iterable = [
                                        openapi_client.models.referenced_website.ReferencedWebsite(
                                            id = '', )
                                        ], ), 
                                interacted = , 
                                tags = openapi_client.models.flattened_tags.FlattenedTags(
                                    iterable = [
                                        openapi_client.models.referenced_tag.ReferencedTag(
                                            id = '', )
                                        ], ), 
                                sensitives = openapi_client.models.flattened_sensitives.FlattenedSensitives(
                                    iterable = [
                                        openapi_client.models.referenced_sensitive.ReferencedSensitive(
                                            id = '', )
                                        ], ), 
                                persons = openapi_client.models.flattened_persons.FlattenedPersons(
                                    iterable = [
                                        openapi_client.models.referenced_person.ReferencedPerson(
                                            id = '', )
                                        ], ), 
                                curated = True, 
                                discovered = True, 
                                activities = openapi_client.models.flattened_activities.FlattenedActivities(
                                    iterable = [
                                        openapi_client.models.referenced_activity.ReferencedActivity(
                                            id = '', )
                                        ], ), 
                                score = , 
                                favorited = True, 
                                pseudo = True, 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], ), 
                                hints = openapi_client.models.flattened_hints.FlattenedHints(
                                    iterable = [
                                        openapi_client.models.referenced_hint.ReferencedHint(
                                            id = '', )
                                        ], ), 
                                anchors = openapi_client.models.flattened_anchors.FlattenedAnchors(
                                    iterable = [
                                        openapi_client.models.referenced_anchor.ReferencedAnchor(
                                            id = '', )
                                        ], ), 
                                conversations = openapi_client.models.flattened_conversations.FlattenedConversations(
                                    iterable = [
                                        openapi_client.models.referenced_conversation.ReferencedConversation(
                                            id = '', )
                                        ], ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = , ),
                messages = openapi_client.models.flattened_conversation_messages.FlattenedConversationMessages(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    iterable = [
                        openapi_client.models.referenced_conversation_message.ReferencedConversationMessage(
                            id = '', 
                            reference = openapi_client.models.flattened_conversation_message.FlattenedConversationMessage(
                                id = '', 
                                created = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                updated = openapi_client.models.grouped_timestamp.GroupedTimestamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    readable = 'Last week - June 3rd, 3:33 a.m.', ), 
                                deleted = , 
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
                                fragment = openapi_client.models.fragment_format.FragmentFormat(
                                    string = openapi_client.models.transferable_string.TransferableString(
                                        raw = '', 
                                        base64 = '', 
                                        base64_url = '', 
                                        data_url = '', ), 
                                    metadata = openapi_client.models.fragment_metadata.FragmentMetadata(
                                        ext = 'csx', ), ), 
                                conversation = openapi_client.models.referenced_conversation.ReferencedConversation(
                                    id = '', ), 
                                sentiment = 'LIKE', 
                                role = 'USER', 
                                score = openapi_client.models.score.Score(
                                    manual = 56, 
                                    automatic = 56, 
                                    priority = 56, 
                                    reuse = 56, 
                                    update = 56, ), 
                                annotations = openapi_client.models.flattened_annotations.FlattenedAnnotations(
                                    iterable = [
                                        openapi_client.models.referenced_annotation.ReferencedAnnotation(
                                            id = '', )
                                        ], 
                                    indices = {
                                        'key' : 56
                                        }, ), ), )
                        ], 
                    indices = {
                        'key' : 56
                        }, 
                    score = openapi_client.models.score.Score(
                        manual = 56, 
                        automatic = 56, 
                        priority = 56, 
                        reuse = 56, 
                        update = 56, ), ),
                options = openapi_client.models.qgpt_relevance_input_options.QGPTRelevanceInputOptions(
                    schema = openapi_client.models.embedded_model_schema.EmbeddedModelSchema(
                        migration = 56, 
                        semantic = 'MAJOR_0_MINOR_0_PATCH_1', ), 
                    database = True, 
                    question = True, ),
                application = '',
                model = ''
            )
        else:
            return QGPTRelevanceInput(
                query = '',
        )
        """

    def testQGPTRelevanceInput(self):
        """Test QGPTRelevanceInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
