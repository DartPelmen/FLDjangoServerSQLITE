from django.db import models


# Модель данных: что хранится в БД.
# Модель не привязана к СУБД.
# Это дает возможность использовать разные СУБД без переписывания кода.
class Table1(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')  # Field name made lowercase.
    data1 = models.CharField(db_column='data1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data2 = models.CharField(db_column='data2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data3 = models.CharField(db_column='data3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data4 = models.CharField(db_column='data4', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table1'
