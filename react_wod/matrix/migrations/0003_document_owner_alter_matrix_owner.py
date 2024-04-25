# Generated by Django 4.2.11 on 2024-04-25 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matrix', '0002_remove_matrix_documents_document_file_contents_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owned_documents', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matrix',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_matricies', to=settings.AUTH_USER_MODEL),
        ),
    ]
