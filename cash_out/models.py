from django.db import models


# Create your models here.

def help_txt_money() -> str:
    """
    Description for incom outcom money
    Color text red
    :return:
    """
    text = """
        <p style="color:red">Не змінювати</p>
    """
    return text


class Reasons(models.Model):
    """
    Reasons for money
    """
    name = models.CharField(
        verbose_name="Причина скидання:",
        max_length=100,
        help_text="Максимальна довжина 100 символів",
    )
    date_time_create = models.DateTimeField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class SenderMoney(models.Model):
    """
    List peoples who send money
    """
    name = models.CharField(
        verbose_name="Ім'я",
        max_length=100,
        help_text="Максимальна довжина 100 символів",
    )
    surname = models.CharField(
        verbose_name="Фамілія",
        max_length=100,
        help_text="Максимальна довжина 100 символів. Не обов'язкове.",
        blank=True, null=True,
    )
    other_info = models.CharField(
        verbose_name="Примітка",
        help_text="Додайте примітку до платника. Не обов'язкове.",
        max_length=100,
        blank=True, null=True,
    )
    date_time_create = models.DateTimeField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} {self.surname}"


class IncomingMoney(models.Model):
    """
    If money incoming
    """
    type_oper = models.CharField(
        verbose_name="Тип операції",
        max_length=30,
        default="Incom",
        help_text=help_txt_money,
    )
    who_send = models.ForeignKey(
        SenderMoney,
        on_delete=models.CASCADE,
        related_name="who",
    )
    count_money = models.SmallIntegerField(
        verbose_name="К-ть грн(одна людина).",
    )
    rsn = models.ForeignKey(
        Reasons,
        on_delete=models.CASCADE,
        related_name="reason_in"
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.who_send.name} {self.who_send.surname} ({self.type_oper})"


class OutcomingMoney(models.Model):
    """
    If money out
    """
    type_oper = models.CharField(
        verbose_name="Тип операції",
        max_length=30,
        default="Outcoming",
        help_text=help_txt_money,
    )
    count_money = models.SmallIntegerField(
        verbose_name="Сумма.",
    )
    rsn = models.ForeignKey(
        Reasons,
        on_delete=models.CASCADE,
        related_name="reason_out",
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.rsn} ({self.type_oper})"
