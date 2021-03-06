from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('ingredients', models.TextField(max_length=1024)),
                ('description', models.TextField(max_length=2048)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('preparation_time', models.PositiveSmallIntegerField()),
                ('votes', models.SmallIntegerField(default=0)),
            ],
        ),
    ]