from django.contrib import admin

# Register your models here.

from .models import (
    Reasons,
    SenderMoney,
    IncomingMoney,
    OutcomingMoney,
)


@admin.register(Reasons)
class ReasonsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date_time_create",
    ]
    search_fields = [
        "name",
    ]


@admin.register(SenderMoney)
class SenderMoneyAdmin(admin.ModelAdmin):
    list_display = [
        "surname",
        "name",
    ]


@admin.register(IncomingMoney)
class IncomingMoneyAdmin(admin.ModelAdmin):
    list_display = [
        "who_send",
        "count_money",
        "date_create",
        "time_create",
        "rsn",
    ]
    raw_id_fields = [
        "who_send",
        "rsn",
    ]
    list_filter = [
        "who_send",
        "rsn",
    ]


@admin.register(OutcomingMoney)
class OutcomingMoneyAdmin(admin.ModelAdmin):
    list_display = [
        "count_money",
        "date_create",
        "time_create",
        "rsn",
    ]
    raw_id_fields = [
        "rsn",
    ]
    list_filter = [
        "rsn",
    ]
