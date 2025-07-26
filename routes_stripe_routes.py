import stripe
import os
from fastapi import APIRouter, Request
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class CheckoutRequest(BaseModel):
    email: str

@router.post("/subscribe")
def create_checkout_session(data: CheckoutRequest):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=data.email,
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Men's App Subscription"},
                    "unit_amount": 599,  # $5.99 in cents
                    "recurring": {"interval": "month"}
                },
                "quantity": 1
            }],
            mode="subscription",
            success_url="https://yourdomain.com/success",
            cancel_url="https://yourdomain.com/cancel"
        )
        return {"checkout_url": session.url}
    except Exception as e:
        return {"error": str(e)}

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        if event["type"] == "checkout.session.completed":
            print("✅ Subscription successful")
        return {"status": "ok"}
    except stripe.error.SignatureVerificationError:
        return {"error": "Webhook signature verification failed"}
