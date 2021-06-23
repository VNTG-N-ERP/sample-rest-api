from django.db import models


# Create your models here.
class Codes(models.Model):
    code_type = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=20, null=False)
    code_name = models.CharField(max_length=100, null=True)
    sort_seq = models.IntegerField()
    use_yn = models.BooleanField()
    remark = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}.{} - {}'.format(self.code_type, self.code, self.code_name)
