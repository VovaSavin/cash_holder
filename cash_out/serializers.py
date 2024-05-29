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


class ReasonsSerializer(serializers.ModelSerializer):
    """
    Serializer for Reason model
    """

    class Meta:
        model = Reasons
        fields = [
            "id",
            "name",
            "date_time_create",
        ]


class IncomingMoneySerializer(serializers.ModelSerializer):
    who_send = SenderMoneySerializer()
    rsn = ReasonsSerializer()

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


class IncomingMoneyShortSerializer(serializers.ModelSerializer):
    """
    For senders
    """
    rsn = ReasonsSerializer()

    class Meta:
        model = IncomingMoney
        fields = [
            "id",
            "type_oper",
            "count_money",
            "rsn",
            "date_create",
            "time_create",
        ]


class IncomingMoneyForReasonSerializer(serializers.ModelSerializer):
    """
    For senders
    """

    class Meta:
        model = IncomingMoney
        fields = [
            "id",
            "type_oper",
            "count_money",
            "date_create",
            "time_create",
        ]


class ReasonFullInfoSerializer(serializers.ModelSerializer):
    """
    Reason with incoming money for it
    """
    reason_in = IncomingMoneyForReasonSerializer(many=True)

    class Meta:
        model = Reasons
        fields = [
            "id",
            "name",
            "reason_in",
            "date_time_create",
        ]


class SenderMoneyFullSerializer(SenderMoneySerializer):
    """
    Sender full info serializer (inherit)
    """

    who = IncomingMoneyShortSerializer(many=True)

    class Meta(SenderMoneySerializer.Meta):
        fields = SenderMoneySerializer.Meta.fields
        fields += [
            "other_info",
            "date_time_create",
            "who",
        ]


class OutcomingMoneySerializer(serializers.ModelSerializer):
    """OutcomingMoney"""

    rsn = ReasonsSerializer()

    class Meta:
        model = OutcomingMoney
        fields = [
            "id",
            "type_oper",
            "count_money",
            "rsn",
            "date_create",
            "time_create",
        ]
