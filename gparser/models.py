from django.db import models


class News(models.Model):
    pic = models.URLField(
        max_length=250,  null=False, verbose_name="Pic_link"
        )
    link = models.URLField(
        max_length=250, unique=True, null=False, verbose_name="Article_link"
        )
    title = models.CharField(
        max_length=300, null=False, verbose_name="Title"
        )
    date = models.DateTimeField(
        auto_now=False, auto_now_add=False, verbose_name="Posting_date"
        )

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'All_News'
        ordering = ['-date']

    def __str__(self):
        return self.title