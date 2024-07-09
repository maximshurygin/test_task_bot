import yookassa

import config


class YookassaPayment:
    secret_key = None
    shop_id = None

    def __init__(self, secret_key, shop_id):
        self.secret_key = secret_key
        self.shop_id = shop_id

    def create_payment(self, amount):
        yookassa.Configuration.account_id = self.shop_id
        yookassa.Configuration.secret_key = self.secret_key

        payment = yookassa.Payment.create({
            "amount": {
                "value": amount,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": config.RETURN_URL_FOR_YOOKASSA_PAYMENT
            },
            "description": "Тестовая оплата 2 руб",
            "capture": True
        })

        url = payment.confirmation.confirmation_url

        return url


yookassa_service = YookassaPayment(config.YOOKASSA_API_KEY, config.YOOKASSA_SHOP_ID)


def get_yookassa_payment_url(amount):
    payment_url = yookassa_service.create_payment(amount)
    return payment_url
