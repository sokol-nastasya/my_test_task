from django.db import models
from django.contrib.auth.models import User
import mptt

from mptt.models import MPTTModel, TreeForeignKey

SHORT_DESCRIPTION = 200


class Keywords(models.Model):
	name = models.CharField(max_length = 50, unique = True)

	def __str__(self):
		return self.name



class Category(MPTTModel):
	name = models.CharField(max_length = 130)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class MPTTMeta:
		order_insertion_by=['name']

mptt.register(Category, order_insertion_by=['name'])

class MainView(models.Model):
	photo = models.ImageField(upload_to = 'profile_image', blank = True, null = True)
	service = models.CharField(max_length = 10000)
	author = models.CharField(max_length = 500)
	description = models.TextField()
	access = models.PositiveIntegerField(default = 0)
	category = TreeForeignKey(Category, blank = True, null = True, related_name = 'cat')
	keywords = models.ManyToManyField(Keywords, related_name = "keywords", related_query_name = 'keyword')


	def get_short_description(self):
		if len(self.description) > SHORT_DESCRIPTION:
			return self.description[:SHORT_DESCRIPTION]
		else:
			return self.description

	def __str__(self):
		return self.service

SHORT_TEXT_LEN = 500

class News(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	likes = models.IntegerField(default = 0)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_short_text(self):
		if len(self.text) > SHORT_TEXT_LEN:
			return self.text[:SHORT_TEXT_LEN]
		else:
			return self.text
