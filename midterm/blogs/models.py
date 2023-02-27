from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    owner = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return 'Title: {}, Description: {}, Owner: {}'.format(self.title, self.description, self.owner)
