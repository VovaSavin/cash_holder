from .models import (
    Reasons,
    SenderMoney,
    IncomingMoney,
    OutcomingMoney,
)
from rest_framework import serializers


class SenderMoneySerializer(serializers.ModelSerializer):
    """
    Sender serializer
    """

    class Meta:
        model = SenderMoney
        fields = [
            "id",
            "name",
            "surname",
        ]


class IncomingMoneySerializer(serializers.ModelSerializer):
    who_send = SenderMoneySerializer()

    class Meta:
        model = IncomingMoney
        fields = [
            "id",
            "type_oper",
            "who_send",
            "count_money",
            "rsn",
            "date_create",
            "time_create",
        ]


class ReasonsSerializer(serializers.ModelSerializer):
    """
    Serializer for Reason model
    """

    class Meta:
        model = Reasons
        fields = [
            "id",
            "date_time_create",
        ]


class SenderMoneyFullSerializer(SenderMoneySerializer):
    """
    Sender full info serializer (inherit)
    """

    who = IncomingMoneySerializer(many=True)

    class Meta(SenderMoneySerializer.Meta):
        fields = SenderMoneySerializer.Meta.fields
        fields += [
            "other_info",
            "date_time_create",
            "who",
        ]
