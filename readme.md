# Using DJANGO for backend and VUEJS together a chronicle

## Introduction

Hello! my name is Gabriel,

I do stream coding sometimes at [my twitch channel](https://www.twitch.tv/caruso323) and so on i did a tutorial to integrate Vue to Django using a CRUD example, in this repo i'll try to describe each step and talk a little about it. Fell free to open an issue if you discord on something.

1. [Django](https://github.com/g-orgo/Django-CRUD-with-VUEJS#django-basics)
2. [REST framework](https://github.com/g-orgo/Django-CRUD-with-VUEJS#django-rest-framework-setting-up)
    - [Serializers](https://github.com/g-orgo/Django-CRUD-with-VUEJS#serializers)
    - [Viewsets](https://github.com/g-orgo/Django-CRUD-with-VUEJS#viewsets)
    - [Router](https://github.com/g-orgo/Django-CRUD-with-VUEJS#router)
3. [VUE template integration](https://github.com/g-orgo/Django-CRUD-with-VUEJS#vue-template-integration)
    - [methods](https://github.com/g-orgo/Django-CRUD-with-VUEJS#endpoints)
4. [CRUD](https://github.com/g-orgo/Django-CRUD-with-VUEJS#crud)
    - ["C"rud](https://github.com/g-orgo/Django-CRUD-with-VUEJS#creating-objects-in-db)
    - [c"R"ud](https://github.com/g-orgo/Django-CRUD-with-VUEJS#render-db-callings)
    - [cr"U"d](https://github.com/g-orgo/Django-CRUD-with-VUEJS#changing-info-from-db-objects)
    - [cru"D"](https://github.com/g-orgo/Django-CRUD-with-VUEJS#deleting-db-objects)

## Django basics

Using Django, as specified in [DJANGO documentation](https://www.djangoproject.com/),
to init a project start with

```
    django-admin startproject <YOUR_PROJECT>
```

and so on you separate your application into some kind of modules called apps. Using

```
    python manage.py startapp <YOUR_APP>
```

in your app folder create your urls file`<YOUR_PROJECT>/<YOUR_APP>/urls.py` and use a generic template view to render a template for your application

```
    from django.views.generic import TemplateView

    urlpatterns = [
        ...
        path('', TemplateView.as_view(template_name="<HTML_NAME>")),
    ]

```

you can nest it into your root url file to avoid urls like `(http://<YOUR_DOMAIN>/<YOUR_APP>/<URL_YOU_DECIDE>)`
to do it you need to literally `include()` it in your `urls.py` file inside `<YOUR_PROJECT>/<YOUR_PROJECT>/`. It will look like this:

```
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('<YOUR_APP>.urls')),
    ]
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

Also at `<YOUR_PROJECT>/<YOUR_APP>/` create `viewsets.py`, in other frameworks may be find conceptually similar implementations named "Controllers". A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as `.get()` or `.post()`, and instead provides actions such as `.list()` and `.create()` and it looks like this.

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

router.register(r'<API_ENDPOINT>', GarageViewSet)
```

and at this point you should declare your api endpoint, it will make your URL look similar to `site.com/api/<API_ENDPOINT>`.

`<YOUR_PROJECT>/<YOUR_PROJECT>/urls.py`

```
from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

## Vue template integration

The easiest way to add vue into django template engine is adding it via cdnjs. Create your template root file at `<YOUR_PROJECT>/<YOUR_APP>/templates/<HTML_NAME>.html` and then add template dir into your `settings.py`.

```
TEMPLATES = [
    {
        'DIRS': [BASE_DIR, '/<YOUR_APP>/'
        ],
    },
]
```

So on call for vue _CDN_.

```
    <script
        src="//unpkg.com/vue@latest/dist/vue.min.js"
    ></script>
```

You can use vue-resource to http requests but i do prefer to use axios.

```
    <script
        src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.1/axios.min.js"
        integrity="sha512-bZS47S7sPOxkjU/4Bt0zrhEtWx0y0CRkhEp8IckzK+ltifIIE9EMIMTuT/mEzoIMewUINruDBIR/jJnbguonqQ=="
        crossorigin="anonymous"
    ></script>
```

At the end of `/templates/<HTML_NAME>` create a `<script/>` tag with your vue instance, it should look similar to it:

```
    let app = new Vue({
        el: "#app",
        delimiters: ["[{", "}]"],
    });
```

`el: "<ELEMENT>"` If you're a vue student you know this element should be the id of your root div.
`delimiters: <HTML_VAR_SYNTAX>` Is a vue setting to set the syntax of your vue interpolation inside html.

## Endpoints

You will use [methods()](https://v1.vuejs.org/guide/events.html) from vue to set endpoints for your CRUD (Create, read, update, delete) system. For a c*R*ud call go to your vue instance and add [data()](https://v3.vuejs.org/api/options-data.html#data) with an empty array and add `methods()`, after it call the data from server-side via http request using `axios`.

```
data: {
    object_spots: [],
},
methods: {
    getObjects: function () {
        axios
        .get("api/<API_ENDPOINT>/")
        .then((res) => {
            this.object_spots = res.data;
        })
        .catch((err) => {
            console.log(err);
        });
    },
},
```

`getObjects()` make an axios request to `"/api/"` router declarated in `<YOUR_PROJECT>/<YOUR_PROJECT>/urls.py` and `"/<API_ENDPOINT>/"` declarated in `<YOUR_PROJECT>/<YOUR_PROJECT>/routers.py`. The response of it is the data we want, and `this.object_spots = res.data;` takes the lead to change the data inside this empty array we just created minutes ago in `data()`.

# CRUD

## Render DB callings

For showcase purpose i'll use a simple `</p>` tag to render db pure data. I'm getting it using `getObjects()`, with a simple [created()](https://br.vuejs.org/v2/api/#created) or [mounted()](https://br.vuejs.org/v2/api/#mounted) vue function i'll call for this endpoint.

```
    mounted: function () {
        this.getObjects();
    },
```

As your database is empty it doesn't do much. To check if it's working you can create one item using [django admin site](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#writing-your-first-django-app-part-2) or [django shell](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api) but you can use *C*rud itself for it.

## Creating objects in DB

Django has some middlewares you'll need to deal with, and at this point knowing about [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/3.2/ref/csrf/#module-django.middleware.csrf) can save you some time. In my vue `data()` i'll create an empty slot to turn this job easier.

```
    data: {
        ...
        blank_object: {
            object_name: "empty",
        },
    },
```

And in `methods()` obviously increase an endpoint.

```
    methods: {
        ...
        createObject: function () {
            axios
            .post("api/<API_ENDPOINT>/", this.blank_object, {
                headers: { "X-CSRFTOKEN": csrftoken }
            })
            .then((res) => {
                this.getObjects();
            });
        },
    }
```

Here we have some diferences from the first endpoint such as `this.blank_object` and `{headers: { "X-CSRFTOKEN": <YOUR_CSRFTOKEN> }})`, the first one give data to the request and the other one adds your csrftoken to headers. If you don't know how to get your CSRFTOKEN i used a javascript [cookie lib](https://github.com/js-cookie/js-cookie) to pass through it.

Getting it lib via _CDN_

```
    <script
        src="https://cdn.jsdelivr.net/npm/js-cookie@rc/dist/js.cookie.min.js"
    ></script>

```

Creating a constant to acess it

```
    <script>
        const csrftoken = Cookies.get("csrftoken");

        let app = new Vue({
            ...
        });
    </script>
```

And for last add an event trigger to it, like a button or something

```
    <button v-on:click="createObject()">
        ...
    </button>
```

## Changing info from DB objects

To update info you will need to use object ID, as specified inside Model class in `<YOUR_PROJECT>/<YOUR_APP>/models.py` or [django default primary key field](https://docs.djangoproject.com/en/3.2/topics/db/models/#automatic-primary-key-fields). Add an editing model to `data()` (or use the one you created for *C*rud example):

```
    new_object_name: {
        object_id: "",
        object_name: "",
    },
```

and you'll need to pass this `object_id` as a param to update methods.

```
    updateObject: function (objectId, newObjectData) {
        axios
        .put(`api/<API_ENDPOINT>/${objectId}/`, newObjectData, { // IT'S IMPORTANT TO USE " ` " AS A JAVASCRIPT INTERPOLATION
            headers: { "X-CSRFTOKEN": csrftoken },
        })
        .then((res) => {
            this.getObjects();
        })
    },
```

## Deleting DB objects

Also passing `object_id` param you can create cru*D*.

```
deleteGarage: function (objectId) {
    axios
        .delete(`api/<API_ENDPOINT>/${objectId}/`, {
            headers: { "X-CSRFTOKEN": csrftoken },
        })
        .then((res) => {
            this.getObjects();
        });
},
```

# THE END