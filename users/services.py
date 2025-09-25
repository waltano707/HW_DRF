import stripe
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY
from users.models import Payment

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(payment_amount):
    """Конвертация рублей в доллары."""
    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(payment_amount * rate)


def create_stripe_course():
    """Создание продукта в страйпе."""
    return stripe.Product.create(name=Payment.paid_course.name)


def create_stripe_price(payment_amount):
    """Создание цены в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=payment_amount * 100,
        recurring={"interval": "month"},
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    """Создание сессии на оплату в страйпе."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
