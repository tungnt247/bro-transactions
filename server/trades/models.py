from django.db import models as _
from accounts.models import User


class Transaction(_.Model):
    class Status(_.IntegerChoices):
        PENDING = 1
        CONFIRMED = 2

    status = _.IntegerField(choices=Status.choices)
    description = _.CharField(max_length=254)
    created_at = _.DateTimeField(auto_now_add=True)
    updated_at = _.DateTimeField(auto_now=True)
    users = _.ManyToManyField(User)
