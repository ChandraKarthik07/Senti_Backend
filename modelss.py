# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Channels(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=255)
    channel_id = models.CharField(max_length=255, blank=True, null=True)
    channel_title = models.CharField(max_length=255, blank=True, null=True)
    channel_description = models.TextField(blank=True, null=True)
    total_videos_count = models.IntegerField(blank=True, null=True)
    total_views_count = models.BigIntegerField(blank=True, null=True)
    total_subs_count = models.BigIntegerField(blank=True, null=True)
    partial_likes_count = models.IntegerField(blank=True, null=True)
    partial_comments_count = models.IntegerField(blank=True, null=True)
    partial_views_count = models.BigIntegerField(blank=True, null=True)
    channel_created_date = models.CharField(max_length=255, blank=True, null=True)
    channel_logo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Channels'


class CommentsSentimentanalysis(models.Model):
    vid = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)
    comment_id = models.CharField(primary_key=True, max_length=255)
    comment = models.TextField(blank=True, null=True)
    sentiment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comments_SentimentAnalysis'


class EmojiFrequency(models.Model):
    vid = models.OneToOneField('Videos', models.DO_NOTHING, primary_key=True)
    highlvl_freq = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emoji_Frequency'


class Monthlystats(models.Model):
    monthly_stats_id = models.AutoField(primary_key=True)
    channel = models.ForeignKey(Channels, models.DO_NOTHING, to_field='channel_id', blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    channel_subs = models.CharField(max_length=255, blank=True, null=True)
    overall_views = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MonthlyStats'
        unique_together = (('channel', 'date'),)


class Scaninfo(models.Model):
    scan_index = models.AutoField(primary_key=True)
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.CharField(max_length=255, blank=True, null=True)
    phase = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScanInfo'
        unique_together = (('scan_id', 'channel_id', 'phase'),)


class Videostats(models.Model):
    video_stats_id = models.AutoField(primary_key=True)
    channel = models.ForeignKey(Channels, models.DO_NOTHING, to_field='channel_id', blank=True, null=True)
    vid_id = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    vid_title = models.CharField(max_length=255, blank=True, null=True)
    vid_view_cnt = models.IntegerField(blank=True, null=True)
    vid_like_cnt = models.IntegerField(blank=True, null=True)
    vid_comment_cnt = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VideoStats'
        unique_together = (('channel', 'vid_id', 'category'),)


class VideoRankings(models.Model):
    vid_rank_id = models.CharField(primary_key=True, max_length=255)
    vid = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    results_vidid = models.CharField(db_column='results_vidID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_vidurl = models.CharField(max_length=255, blank=True, null=True)
    results_vidtitle = models.CharField(db_column='results_vidTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_viddesc = models.TextField(db_column='results_vidDesc', blank=True, null=True)  # Field name made lowercase.
    results_vidduration = models.CharField(db_column='results_vidDuration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_vidviewcnt = models.CharField(db_column='results_vidViewcnt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_viddt = models.CharField(db_column='results_vidDt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Video_Rankings'


class Videos(models.Model):
    vid_id = models.CharField(primary_key=True, max_length=255)
    channel = models.ForeignKey(Channels, models.DO_NOTHING, to_field='channel_id', blank=True, null=True)
    vid_title = models.CharField(max_length=255, blank=True, null=True)
    vid_view_cnt = models.IntegerField(blank=True, null=True)
    vid_like_cnt = models.IntegerField(blank=True, null=True)
    vid_comment_cnt = models.IntegerField(blank=True, null=True)
    vid_url = models.CharField(max_length=255, blank=True, null=True)
    vid_desc = models.TextField(blank=True, null=True)
    vid_duration = models.CharField(max_length=255, blank=True, null=True)
    vid_published_at = models.CharField(max_length=255, blank=True, null=True)
    vid_thumbnail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Videos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CoreCustomapplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    post_logout_redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    skip_authorization = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    algorithm = models.CharField(max_length=5)
    user = models.ForeignKey('CoreUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_customapplication'


class CoreScantable(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=255)
    channel_name = models.CharField(max_length=255, blank=True, null=True)
    scan_date = models.CharField(max_length=255)
    user = models.ForeignKey('CoreUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_scantable'


class CoreUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_user'


class CoreUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_user_groups'
        unique_together = (('user', 'group'),)


class CoreUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Oauth2ProviderAccesstoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    scope = models.TextField()
    application = models.ForeignKey('Oauth2ProviderApplication', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    source_refresh_token = models.OneToOneField('Oauth2ProviderRefreshtoken', models.DO_NOTHING, blank=True, null=True)
    id_token = models.OneToOneField('Oauth2ProviderIdtoken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_accesstoken'


class Oauth2ProviderApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.CharField(unique=True, max_length=100)
    redirect_uris = models.TextField()
    client_type = models.CharField(max_length=32)
    authorization_grant_type = models.CharField(max_length=32)
    client_secret = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING, blank=True, null=True)
    skip_authorization = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    algorithm = models.CharField(max_length=5)
    post_logout_redirect_uris = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_application'


class Oauth2ProviderGrant(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    expires = models.DateTimeField()
    redirect_uri = models.TextField()
    scope = models.TextField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    code_challenge = models.CharField(max_length=128)
    code_challenge_method = models.CharField(max_length=10)
    nonce = models.CharField(max_length=255)
    claims = models.TextField()

    class Meta:
        managed = False
        db_table = 'oauth2_provider_grant'


class Oauth2ProviderIdtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    jti = models.CharField(unique=True, max_length=32)
    expires = models.DateTimeField()
    scope = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_idtoken'


class Oauth2ProviderRefreshtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    access_token = models.OneToOneField(Oauth2ProviderAccesstoken, models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(Oauth2ProviderApplication, models.DO_NOTHING)
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    revoked = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth2_provider_refreshtoken'
        unique_together = (('token', 'revoked'),)


class SocialAuthAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(CoreUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
