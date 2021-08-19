# Generated by Django 3.1.13 on 2021-08-19 13:52

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("dcim", "0005_device_local_context_schema"),
        ("extras", "0010_change_cf_validation_max_min_field_to_bigint"),
        ("nautobot_plugin_device_lifecycle_mgmt", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SoftwareLCM",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("version", models.CharField(max_length=50)),
                ("alias", models.CharField(blank=True, max_length=50, null=True)),
                ("end_of_support", models.DateField(blank=True, null=True)),
                ("end_of_security_patches", models.DateField(blank=True, null=True)),
                ("documentation_url", models.URLField(blank=True)),
                ("download_url", models.URLField(blank=True)),
                ("image_file_name", models.CharField(blank=True, max_length=100)),
                ("image_file_checksum", models.CharField(blank=True, max_length=256)),
                ("long_term_support", models.BooleanField(default=False)),
                ("pre_release", models.BooleanField(default=False)),
                ("device_platform", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="dcim.platform")),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "verbose_name": "Software",
                "ordering": ("end_of_support", "end_of_security_patches"),
                "unique_together": {("device_platform", "version")},
            },
        ),
        migrations.CreateModel(
            name="ValidatedSoftwareLCM",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("assigned_to_object_id", models.UUIDField()),
                ("start", models.DateField()),
                ("end", models.DateField(blank=True, null=True)),
                ("preferred", models.BooleanField(default=False)),
                (
                    "assigned_to_content_type",
                    models.ForeignKey(
                        limit_choices_to=models.Q(
                            ("app_label", "dcim"), ("model__in", ("device", "devicetype", "inventoryitem"))
                        ),
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "software",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nautobot_plugin_device_lifecycle_mgmt.softwarelcm",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "verbose_name": "Validated Software",
                "ordering": ("software", "preferred", "start"),
                "unique_together": {("software", "assigned_to_content_type", "assigned_to_object_id")},
            },
        ),
    ]
