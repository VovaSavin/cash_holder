# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    IncomingMoney,
    OutcomingMoney,
    Reasons,
    SenderMoney,
)
from .serializers import (
    IncomingMoneySerializer,
    OutcomingMoneySerializer,
    ReasonsSerializer,
    SenderMoneySerializer,
    SenderMoneyFullSerializer,
    ReasonFullInfoSerializer,
)


# Create your views here.


class IncomingMoneyAPI(APIView):
    """
    Show list money in
    """

    def get(self, request):
        list_in = IncomingMoney.objects.all()
        serializer = IncomingMoneySerializer(list_in, many=True)
        return Response(serializer.data)


class OutgoingMoneyAPI(APIView):
    """
    Out money
    """

    def get(self, request):
        qw_out_list = OutcomingMoney.objects.all()
        serializer = OutcomingMoneySerializer(qw_out_list, many=True)
        return Response(serializer.data)


class SendersAPI(APIView):
    def get(self, request):
        senders_qw = SenderMoney.objects.all()
        serializer = SenderMoneyFullSerializer(senders_qw, many=True)
        return Response(serializer.data)


class AllReasonAPI(APIView):

    def get(self, request):
        rsn_qw = Reasons.objects.all()
        serializer = ReasonFullInfoSerializer(rsn_qw, many=True)
        return Response(serializer.data)
