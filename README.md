# My Notes

## Background
A simple app to understand the Django test functions and other features. Using a tutorial from [django tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) to learn more about the concepts that I find difficult to grasp in **ponderous_grasshopper**. I will start this new project to learn about tests.

## The **polls** app

About the **poll** application, 

- Question “index” page – displays the latest few questions.
- Question “detail” page – displays a question text, with no results but with a form to vote.
- Question “results” page – displays results for a particular question.
- Vote action – handles voting for a particular choice in a particular question.

# My Notes



## Use **django.test.Client**

Add **testserver** to **ALLOWED_HOSTS**  in the **.env**.

## Monitor the stream logs in Azure

Use the `az` cli.

`az webapp log tail --name appname --resource-group myResourceGroup`


## Default admin template directory

Custom Admin site is **not working**.
Create a **admin** inside the **polls templates**.
`/polls/templates/admin/`.

Default templates can be found at [django/contrib/admin/templates](https://github.com/django/django/blob/main/django/contrib/admin/templates).


## Using namespace in STATICFILES_DIRS

25 Jul, Thu

The **static** files setting is confusing. Now, I add a namespace to the **STATICFILES_DIRS**. The [**prefixes**](https://docs.djangoproject.com/en/5.0/ref/settings/#prefixes-optional) is explained in Django Docs.

```
# The files are in actual location:
# "./polls/static/polls" (./appname/static/appname) format

# Do not specify the staticfiles_dirs
STATICFILES_DIRS = [ ]

# Refer to the staticfiles like this:
<link rel="stylesheet" href="{% static 'polls/styles.css' %}">
<link rel="icon" href="{% static 'polls/favicon.svg' %}">

# Make a directory "images/" under the "polls/static/polls".
# So the directory is now like this "polls/static/polls/images/"
# To refer to the image in styles.css:
h1 {
    background: lightgreen url("images/pumpkin.jpg") no-repeat;
   }
```

```
# This is another way.
STATICFILES_DIRS = [
    #BASE_DIR / "polls" / "static",
    ("my_polls", "./polls/static/polls/"),
]

# Refer to the static files like this:
<link rel="stylesheet" href="/static/my_polls/styles.css">
```


## Using **coverage**

Run the **coverage** like this:

```
coverage run manage.py test polls.tests.test_question

coverage html
```



## Saving object with F() and retrieve the object again

24 Jul, Thu

When an object with saved with `django.db.models.F`, the object is in database.
The latest value of the object is in database also. If we need the value of the object, we need to retrive the object again.

```
print(f"\tCurrent votes: {selected_choice.votes}")
>>> 10
selected_choice.votes = F("votes") + 1
selected_choice.save()
# After save, we have to retrieve the object again to get
# the latest state of the db.
selected_choice = Choice.objects.get(id=selected_choice.id)
print(f"\tAfter votes: {selected_choice.votes}")
>>> 11
```

## collectstatic

Need to run

```python manage.py collectstatic``` 

for the `{% static 'some_image' %}` to work.

The **base.html** must be in the **project level** templates directory. In this app, this is **\eggplant\templates\base.html**.

The app **polls** templates is in **\polls\templates\polls\index.html** and etc. The **static** folder is in **\polls\static\logo.svg**.

The `favicon.svg` and the logo are using the <em>same</em> svg file. But, the filename must be specified separately. For example, the the logo name must be named something like `logo.svg`.

In the **base.html**, remember to put in the static template tag at the end of the file where the javascript is specified.

```<script defer src={% static "main.js" %}></script>```

## Run tests

The **tests** folders, filenames and individual class and methods must be prefix with **test**.

`python manage.py test polls.tests`


## **reverse()

To get the url:

```
from django.http import HttpResponseRedirect
from django.urls import reverse
# must include the trailing **,** in the args=()
reverse('polls-detail', args=(9, ))
'/polls/9/'
reverse('polls-results', args=(9,))
'/polls/9/results/'
reverse('polls-vote', args=(9,))
'/polls/9/vote/'
# with namespace specified
reverse('admin:index')
'/admin/'
reverse("polls:polls-index")
'/polls/'
reverse("polls:polls-vote", args=(0, ))
'/polls/0/vote/'
```

[Namespaced URLs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#term-instance-namespace) are specified using the ':' operator. For example, the main index page of the admin application is referenced using 'admin:index'. This indicates a namespace of 'admin', and a named URL of 'index'.

Namespaces can also be nested. The named URL 'sports:polls:index' would look for a pattern named 'index' in the namespace 'polls' that is itself defined within the top-level namespace 'sports'.

The current application can be found from the `request.current_app` attribute.

Namespace can be specified in two ways:
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    ...,
]

# Or, in the main urls.py
from django.urls import include, path

urlpatterns = [
    path("author-polls/", include("polls.urls", namespace="author-polls")),
    path("publisher-polls/", include("polls.urls", namespace="publisher-polls")),
]
```

## Register app in the **admin**

For example, we need to tell the **admin** that **Question** objects have an admin interface. To do this, open the **polls/admin.py** file, and edit it to look like this:

```
# polls/admin.py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## To see the SQL migration commands

The `0001` is the migration number. It prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do.

`python manage.py sqlmigrate polls 0001`

- By convention, Django appends "_id" to the foreign key field name.
- The **migrate** command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called **django_migrations**) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.


## **INSTALLED_APPS** and **migrate**

The **migrate** command looks at the **INSTALLED_APPS** setting and creates any necessary database tables.

In the **INSTALLED_APPS**, it is possible to use:
`polls` or `polls.apps.PollsConfig`. The **PollsConfig** class is in the **polls/apps.py** file, so its dotted path is **'polls.apps.PollsConfig'**. 


## Browser reload

Browser reload module will only work when there is a mapping of urls.

There will see an exception: 
`django.urls.exceptions.NoReverseMatch: 'django_browser_reload' is not a registered namespace`

```
# URLconf
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]

# settings.py
# for browser reload
#'django_browser_reload',
# for browser reload
# The middleware should be listed after any others that encode the 
# response, such as Django’s GZipMiddleware.
#'django_browser_reload.middleware.BrowserReloadMiddleware',
```

## Create a default settings template
19 Jul

Create a **settings.py** for my usage.

## Git steps:

- First, create the repo at GitHub.
- Then at my local folder, do these steps:

```
git init
git branch --show (should see the **main** branch in my own local folder).
git remote add origin https://github.com/liewchooichin/crunchy_cucumber
git fetch
git pull origin main
```
