from django.db.models import DateTimeField, CharField, Model
from datetime import datetime

class CustomDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = datetime.today().isoformat(sep=" ", timespec="seconds")
            setattr(model_instance, self.attname, value)
            return value

class Task(Model):

    user = CharField(max_length=100)
    time = CustomDateTimeField(auto_now_add=True)
    task = CharField(max_length=200)
    tags = CharField(max_length=200, default="-", null=True)

    class Meta:
        ordering = ('-time',)

class Tag(Model):

    # def __str__(self):
    #     return self.tag

    tag = CharField(max_length=20, null=False, default="-", primary_key=True)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"