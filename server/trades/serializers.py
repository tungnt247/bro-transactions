from rest_framework import serializers as _
from .models import TransactionStatus


class TransactionSerializer(_.Serializer):
    status = _.ChoiceField(choices=TransactionStatus.choices)
    description = _.CharField()
    created_at = _.DateTimeField()
    updated_at = _.DateTimeField()
    creator = _.CharField()
    executor = _.CharField()
