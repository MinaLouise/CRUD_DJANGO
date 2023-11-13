from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Todolist(models.Model):
    items = models.TextField()
    complete = models.BooleanField(default=False)



def create_list(items, complete):
    todo_list = Todolist(items=items, complete=complete)
    todo_list.save()
    return todo_list

def view_list():
    return Todolist.objects.all()

def search_list(items):
    try:
        return Todolist.objects.get(items=items)
    except Todolist.DoesNotExist:
        return None

def filter_complete(complete):
    return Todolist.objects.filter(complete=complete)

def update_list(item, completed):
    todo_list = Todolist.objects.get(items=item)
    todo_list.complete = completed
    todo_list.save()
    return todo_list

def delete_item(items):
    todo_list = Todolist.objects.get(items=items)
    todo_list.delete()
    return todo_list