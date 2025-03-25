from djongo import models
from bson import ObjectId
class Data(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True) 
    end_year = models.CharField(max_length=10, blank=True, null=True)
    intensity = models.CharField(max_length=10,blank=True, null=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10, blank=True, null=True)
    impact = models.CharField(max_length=100, blank=True, null=True)
    added = models.DateTimeField()
    published = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    relevance = models.CharField(max_length=10,blank=True, null=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.CharField(max_length=10,blank=True, null=True)
    class Meta:
        db_table = 'json_data_collection'
    def __str__(self):
        return self.title


