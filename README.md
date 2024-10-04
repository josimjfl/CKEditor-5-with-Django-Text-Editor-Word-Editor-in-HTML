# CKEditor 5 Integration in Django



![Screenshot 2024-10-04 180915](https://github.com/user-attachments/assets/acf27088-3f5e-4784-a6c3-2897df664177)

This guide will help you integrate CKEditor 5 into your Django project, customize it with plugins like `lineHeight`, `fontSize`, and configure toolbar options.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Creating Forms](#creating-forms)
- [Customizing the Editor](#customizing-the-editor)
- [CKEditor 5 Configuration](#ckeditor-5-configuration)

---
![Screenshot 2024-10-04 181525](https://github.com/user-attachments/assets/e6702140-3572-4a89-a4f0-a5fccb8bb7b5)

## Installation

### 1. Install `django-ckeditor-5` Package

You can install CKEditor 5 via the `django-ckeditor-5` package.

```bash
pip install django-ckeditor-5
```

### 2. Add to Installed Apps

Update your `settings.py` file to include `django_ckeditor_5`.

```python
INSTALLED_APPS = [
    # other apps
    'django_ckeditor_5',
]
```

### 3. Set up Static and Media Files

Add the following settings in `settings.py` for media and static file handling:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

---

## Configuration

### 1. Add CKEditor to the Admin or Your Forms

To use CKEditor in forms, create or update your forms by specifying `CKEditor5Widget` for text fields.

```python
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text')
        widgets = {
            'text': CKEditor5Widget(config_name='default')
        }
```

### 2. Add CKEditor to a Template

In your HTML template, load the required static files and include the form:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CKEditor 5 Integration</title>
    
    {{ form.media }} <!-- Required for CKEditor5 styling/js -->

    <style>
        .main-container {
            width: 80%;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>CKEditor 5 with Django</h1>

        <!-- Display articles (optional) -->
        <div>
            {% for article in articles %}
                <h2>{{ article.title }}</h2>
                <div>{{ article.text|safe }}</div>
            {% endfor %}
        </div>

        <!-- Form to submit comments or articles -->
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
```

---

## Customizing the Editor

### 1. Create CKEditor Configuration

In your `settings.py`, add a configuration for CKEditor 5:

```python
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'undo', 'redo', '|', 'selectAll', '|', 'bold', 'italic', 'underline', 'strikethrough', '|', 
            'fontSize', 'fontFamily', 'alignment', 'fontColor', 'fontBackgroundColor', '|',
            'lineHeight', '|', 'removeFormat', 'link', 'bulletedList', 'numberedList', 'blockQuote', '|',
            'imageUpload', 'mediaEmbed', 'codeBlock', 'findAndReplace', '|',
            'highlight', 'horizontalLine', 'heading', '|',
            'insertTable', 'tableColumn', 'tableRow', 'mergeTableCells'
        ],
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:alignLeft', 'imageStyle:alignRight'
            ]
        },
        'fontSize': {
            'options': [
                'default', '8pt', '10pt', '12pt', '14pt', '16pt', '18pt', '20pt', '22pt', '24pt', '36pt', '48pt'
            ]
        },
        'alignment': {
            'options': ['left', 'right', 'center', 'justify']
        },
        'lineHeight': {
            'options': ['1', '1.5', '2', '2.5', '3']
        },
        'height': 400,
        'width': '100%',
        'removePlugins': ['CKFinderUploadAdapter', 'EasyImage', 'Base64UploadAdapter']
    }
}
```

### 2. Customize Toolbar and Plugins

The above configuration enables various formatting options including font size, text alignment, line height, and more.

---

## Creating Forms

In your `forms.py` file, you can use the customized CKEditor 5 widget in the `widgets` argument.

Example:

```python
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text')
        widgets = {
            'text': CKEditor5Widget(config_name='default')
        }
```

---

## Running the Project

### 1. Run Migrations

If you're using a new model for articles or comments, make sure to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Start the Django Server

Run your Django server to see CKEditor in action:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to test the CKEditor integration.

---

## Conclusion

This guide provides a simple integration of CKEditor 5 in Django using the `django-ckeditor-5` package. It also demonstrates how to customize the toolbar and add extra plugins for features like font size, alignment, and line height.

--- 

