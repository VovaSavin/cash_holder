from django.urls import path
from .views import (
    IncomingMoneyAPI,
    OutgoingMoneyAPI,
    SendersAPI,
    AllReasonAPI,
)

urlpatterns = [
    path("incoming-money/", IncomingMoneyAPI.as_view(), name="incoming"),
    path("outgoing-money/", OutgoingMoneyAPI.as_view(), name="outgoing"),
    path("senders/", SendersAPI.as_view(), name="senders"),
    path("reasons/", AllReasonAPI.as_view(), name="rsns"),
]
