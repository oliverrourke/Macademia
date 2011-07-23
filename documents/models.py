from django.db import models

class File(models.Model):	
	file_name  = models.CharField(max_length=50)
	file_path = models.CharField(max_length=200)
	parent_folder = models.IntegerField()
	created_on = models.DateTimeField()
	created_by = models.IntegerField()
	last_updated_on = models.DateTimeField()
	last_updated_by = models.IntegerField()

class Folder(models.Model):
	name = models.CharField(max_length=200)
	parent_folder = models.IntegerField()
	folder_path = models.CharField(max_length=200)
	
class Comment(models.Model):
	content = models.CharField(max_length = 1000)
	created_by = models.IntegerField()
	created_on = models.DateTimeField()
	attached_to_type = models.IntegerField() #0 for Folder, 1 for File, 2 for Comment (potential to include more)
	attached_to_id = models.IntegerField()