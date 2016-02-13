# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from wagtail.wagtailcore.utils import validate_unicode_slug

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0011_page_first_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(
                validators=[validate_unicode_slug],
                help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/',
                max_length=255
            ),
            preserve_default=True,
        ),
    ]
