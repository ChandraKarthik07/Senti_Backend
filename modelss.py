# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Channels(models.Model):
    scan_id = models.CharField(primary_key=True, max_length=255)  # The composite primary key (scan_id, channel_id) found, that is not supported. The first column is selected.
    channel_id = models.CharField(max_length=255)
    channel_title = models.CharField(max_length=255, blank=True, null=True)
    channel_description = models.TextField(blank=True, null=True)
    total_videos_count = models.IntegerField(blank=True, null=True)
    total_views_count = models.IntegerField(blank=True, null=True)
    total_subs_count = models.IntegerField(blank=True, null=True)
    partial_likes_count = models.IntegerField(blank=True, null=True)
    partial_comments_count = models.IntegerField(blank=True, null=True)
    partial_views_count = models.IntegerField(blank=True, null=True)
    channel_created_date = models.CharField(max_length=255, blank=True, null=True)
    channel_logo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Channels'
        unique_together = (('scan_id', 'channel_id'),)


class CommentsSentimentanalysis(models.Model):
    vid = models.OneToOneField('Videos', models.DO_NOTHING, primary_key=True)  # The composite primary key (vid_id, comment_id) found, that is not supported. The first column is selected.
    comment_id = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    sentiment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comments_SentimentAnalysis'
        unique_together = (('vid', 'comment_id'),)


class EmojiFrequency(models.Model):
    vid = models.OneToOneField('Videos', models.DO_NOTHING, primary_key=True)
    highlvl_freq = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Emoji_Frequency'


class Monthlystats(models.Model):
    channel = models.OneToOneField(Channels, models.DO_NOTHING, primary_key=True)  # The composite primary key (channel_id, date) found, that is not supported. The first column is selected.
    date = models.CharField(max_length=255)
    channel_subs = models.CharField(max_length=255, blank=True, null=True)
    overall_views = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MonthlyStats'
        unique_together = (('channel', 'date'),)


class Scaninfo(models.Model):
    scan_id = models.CharField(max_length=255, blank=True, null=True)
    channel_id = models.CharField(primary_key=True, max_length=255)  # The composite primary key (channel_id, phase) found, that is not supported. The first column is selected.
    phase = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ScanInfo'
        unique_together = (('channel_id', 'phase'),)


class Videostats(models.Model):
    channel = models.OneToOneField(Channels, models.DO_NOTHING, primary_key=True)  # The composite primary key (channel_id, vid_id, category) found, that is not supported. The first column is selected.
    vid_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255, blank=True, null=True)
    vid_title = models.CharField(max_length=255, blank=True, null=True)
    vid_view_cnt = models.CharField(max_length=255, blank=True, null=True)
    vid_like_cnt = models.CharField(max_length=255, blank=True, null=True)
    vid_comment_cnt = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'VideoStats'
        unique_together = (('channel', 'vid_id', 'category'),)


class VideoRankings(models.Model):
    vid = models.OneToOneField('Videos', models.DO_NOTHING, primary_key=True)  # The composite primary key (vid_id, keyword, results_vidID) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=255)
    results_vidid = models.CharField(db_column='results_vidID', max_length=255)  # Field name made lowercase.
    results_vidurl = models.CharField(max_length=255, blank=True, null=True)
    results_vidtitle = models.CharField(db_column='results_vidTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_viddesc = models.TextField(db_column='results_vidDesc', blank=True, null=True)  # Field name made lowercase.
    results_vidduration = models.CharField(db_column='results_vidDuration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_vidviewcnt = models.CharField(db_column='results_vidViewcnt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    results_viddt = models.CharField(db_column='results_vidDt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Video_Rankings'
        unique_together = (('vid', 'keyword', 'results_vidid'),)


class Videos(models.Model):
    channel = models.OneToOneField(Channels, models.DO_NOTHING, primary_key=True)  # The composite primary key (channel_id, vid_id) found, that is not supported. The first column is selected.
    vid_id = models.CharField(max_length=255)
    vid_title = models.CharField(max_length=255, blank=True, null=True)
    vid_view_cnt = models.IntegerField(blank=True, null=True)
    vid_like_cnt = models.IntegerField(blank=True, null=True)
    vid_comment_cnt = models.IntegerField(blank=True, null=True)
    vid_url = models.CharField(max_length=255, blank=True, null=True)
    vid_desc = models.TextField(blank=True, null=True)
    vid_duration = models.CharField(max_length=255, blank=True, null=True)
    vid_published_at = models.TextField(blank=True, null=True)
    vid_thumbnail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Videos'
        unique_together = (('channel', 'vid_id'),)
