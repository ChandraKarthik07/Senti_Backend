


from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
import uuid
import pytz
from oauth2_provider.models import AbstractApplication

class CustomUserManager(UserManager):
    pass

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the form of +919999999999.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    # otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomUserManager()
    # USERNAME_FIELD="email"
    # REQUIRED_FIELDS=[]

    def __str__(self):
        return f"{self.username}-{self.id}"
    class meta:
        db_table = 'User'


User._meta.get_field('groups').remote_field.related_name = 'user_replica_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_replica_permissions'



class CustomApplication(AbstractApplication):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class scanTable(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    scan_id=models.CharField(primary_key=True, max_length=255)
    channel_name=models.CharField(max_length=255, blank=True, null=True)
    scan_date=models.CharField(max_length=255)


class Channels(models.Model):
    scan_id = models.OneToOneField(scanTable,primary_key=True, max_length=255, to_field='scan_id', db_column='scan_id', on_delete=models.CASCADE)
    channel_id = models.CharField(max_length=255, blank=True, null=True,unique=True)
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


class CommentsSentimentanalysis(models.Model):
    vid = models.ForeignKey(Videos, models.DO_NOTHING, blank=True, null=True)
    comment_id = models.CharField(primary_key=True, max_length=255)
    comment = models.TextField(blank=True, null=True)
    sentiment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comments_SentimentAnalysis'


class EmojiFrequency(models.Model):
    vid = models.OneToOneField(Videos, models.DO_NOTHING, primary_key=True,to_field="vid_id")
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
    vid = models.ForeignKey(Videos, models.DO_NOTHING, blank=True, null=True)
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


