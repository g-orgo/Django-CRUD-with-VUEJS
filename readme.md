# Using DJANGO for backend and VUEJS together a chronicle

## Introduction

Hello, I'll try to describe each step and talk a little about it,
fell free to open an issue if you discord on something.

1. [Django](https://github.com/g-orgo/Django-CRUD-with-VUEJS#django-basics)
2. [REST framework](https://github.com/g-orgo/Django-CRUD-with-VUEJS#django-rest-framework-setting-up)
    - [Serializers](https://github.com/g-orgo/Django-CRUD-with-VUEJS#serializers)
    - [Viewsets](https://github.com/g-orgo/Django-CRUD-with-VUEJS#viewsets)
    - [Router](https://github.com/g-orgo/Django-CRUD-with-VUEJS#router)
3. [VUE template integration](https://github.com/g-orgo/Django-CRUD-with-VUEJS#vue-template-integration)
    - [methods](https://github.com/g-orgo/Django-CRUD-with-VUEJS#methods)

## Django basics

To Django, as specified in [DJANGO documentation](https://www.djangoproject.com/),
to init a project start with

```
    django-admin startproject <YOUR_PROJECT>
```

and so on you separate your application into some kind of modules called apps. Using

```
    python manage.py startapp <YOUR_APP>
```

## Django REST framework setting up

then you'll install [Django REST framework](https://www.django-rest-framework.org/)
using

```
    pip install djangorestframework
```

and add both of them into your `INSTALED_APPS` list, on `<YOUR_PROJECT>/<YOUR_PROJECT>/settings.py`

```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        '<YOUR_APP>'
        ]
```

after it you'll need to create [serializers](https://www.django-rest-framework.org/api-guide/serializers/#serializers), [viewsets](https://www.django-rest-framework.org/api-guide/viewsets/#viewsets) and [routers](https://www.django-rest-framework.org/api-guide/routers/#routers) about your models at `<YOUR_PROJECT>/<YOUR_APP>/models.py` for rest framework. I used a garage api to test it so my models look like this

```
    from django.db import models

    class Garage_place(models.Model):
        garage_id = models.AutoField(primary_key=True)
        garage_name = models.CharField(max_length=100)
```

## Serializers

Serializers work very similarly to Django `Form` and `ModelForm` libs, they allow complex data such as querysets and model instances to be converted to native Python datatypes. My serializer file (you will need to create it), located in `<YOUR_PROJECT>/<YOUR_APP>/serializers.py`, look like this...

```
    from rest_framework import serializers
    from .models import Garage_place

    class GarageSerializer(serializers.ModelSerializer):
        class Meta:
            model = Garage_place
            fields = '__all__'
```

## Viewsets

Also at `<YOUR_PROJECT>/<YOUR_APP>/`, `viewsets.py` in other frameworks may be find conceptually similar implementations named something like "Controllers". A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as `.get()` or `.post()`, and instead provides actions such as `.list()` and `.create()` and it looks like this.

```
    from rest_framework import viewsets
    from .models import Garage_place
    from .serializers import GarageSerializer

    class GarageViewSet(viewsets.ModelViewSet):
        queryset = Garage_place.objects.all()
        serializer_class = GarageSerializer
```

## Router

Routers adds support for automatic URL routing to Django, and provides you with a simple, quick and consistent way of wiring your view logic to a set of URLs. So it's better to leave it in `<YOUR_PROJECT>/<YOUR_PROJECT>/routers.py`.

```
from rest_framework import routers
from <YOUR_APP>.viewsets import GarageViewSet

router = routers.DefaultRouter()

router.register(r'garages', GarageViewSet)
```

and at this point you should declare your api endpoint, it will make your URL look similar to `site.com/api/<SOMETHING>`.

`<YOUR_PROJECT>/<YOUR_PROJECT>/urls.py`

```
from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('base_files.urls')),
]
```

## Vue template integration

The easiest way to add vue into django template engine is adding it via cdnjs using

```
    <script
        src="//unpkg.com/vue@latest/dist/vue.min.js"
    ></script>
```
you can use vue-resource to http requests but i do prefer to use axios.

```
    <script
        src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.1/axios.min.js"
        integrity="sha512-bZS47S7sPOxkjU/4Bt0zrhEtWx0y0CRkhEp8IckzK+ltifIIE9EMIMTuT/mEzoIMewUINruDBIR/jJnbguonqQ=="
        crossorigin="anonymous"
    ></script>
```

## Methods

Methods will be used to set endpoints for your CRUD (Create, read, update, delete)