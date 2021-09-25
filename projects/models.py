from django.db import models


class Project(models.Model):
    '''
    Whilst creating a Project, at least one Dir will
    be mandatory. The items in that Dir will be added
    as Items to a Funnel which will be automatically
    created alongwith the Project. A default Funnel,
    if you will.
    '''
    label = models.CharField(max_length=100)
    created_date = models.DateTimeField('Date created')

    def __str__(self, ):
        return self.label


class Dir(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    # created_date = models.DateTimeField('Date created')
    # votes = models.IntegerField(default=0)

    def __str__(self, ):
        return self.path


class Funnel(models.Model):
    '''
    Whilst creating a Funnel, add items as Items from
    previous Funnel from Project (if exists).
    '''
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    created_date = models.DateTimeField('Date created')

    def __str__(self, ):
        return self.label


class Item(models.Model):
    funnel = models.ForeignKey(Funnel, on_delete=models.CASCADE)
    file_uuid = models.CharField(max_length=255)
    is_selected = models.BooleanField(default=False)
    created_date = models.DateTimeField('Date created')
    modified_date = models.DateTimeField('Date modified')

    def __str__(self, ):
        return f'{self.file_uuid} - {self.is_selected}'
