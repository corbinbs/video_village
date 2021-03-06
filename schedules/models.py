from django.db import models


class Window(models.Model):
    building = models.PositiveIntegerField()
    pi = models.ForeignKey('pis.Pi', null=True, blank=True)


class Schedule(models.Model):
    schedule_start_date = models.DateField()
    schedule_end_date = models.DateField()
    window = models.ForeignKey(Window)

    def __str__(self):
        return self.schedule_date.strftime('%Y-%m-%d') + '  @ Pi:' + str(self.pi)

    class Meta:
        unique_together = (('schedule_start_date', 'window'),)

    def duplicate(self, new_start_date, new_end_date, new_window):
        """
        Duplicate the Schedule to a new date and/or time
        :param new_start_date:
        :param new_end_date:
        :param new_window:
        :return:
        """


class ScheduleItem(models.Model):
    schedule = models.ForeignKey(Schedule, related_name='items')
    video = models.ForeignKey('videos.Video')
    video_start_seconds = models.PositiveIntegerField(null=True, blank=True)
    video_duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    play_order = models.PositiveIntegerField()

    class Meta:
        unique_together = (('schedule', 'play_order'),)

    def __str__(self):
        return str(self.play_order) + ': ' + str(self.video)
