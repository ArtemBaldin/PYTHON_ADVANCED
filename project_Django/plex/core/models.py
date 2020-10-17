from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    age = models.IntegerField(verbose_name="Возраст")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        data = [self.last_name, self.first_name, self.middle_name, self.age]
        return data
