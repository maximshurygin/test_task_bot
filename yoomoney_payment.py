from yoomoney import Client, Quickpay

from uuid import uuid4

import config


# Определяем класс для работы с платежами Yoomoney
class YoomoneyPayment:
    def __init__(self, access_token, receiver):
        # Инициализация клиента Yoomoney с использованием токена доступа
        self.client = Client(access_token)
        # Идентификатор получателя платежа
        self.receiver = receiver

    def generate_payment_url(self, amount, description):
        # Генерация уникальной метки для каждого платежа
        label = str(uuid4())
        # Создание объекта Quickpay для генерации ссылки на оплату
        quickpay = Quickpay(
            receiver=self.receiver,
            quickpay_form="shop",
            targets=description,
            paymentType="SB",
            sum=amount,
            label=label
        )
        # Возвращаем сгенерированную ссылку на оплату и метку платежа
        return quickpay.base_url, label


# Создаем экземпляр класса для работы с платежами
payment_service = YoomoneyPayment(config.YOOMONEY_ACCESS_TOKEN, config.YOOMONEY_CLIENT_ID)


# Функция для генерации ссылки на оплату
def get_payment_url(amount, description):
    # Генерируем ссылку на оплату и метку платежа
    payment_url, label = payment_service.generate_payment_url(amount, description)
    return payment_url, label
