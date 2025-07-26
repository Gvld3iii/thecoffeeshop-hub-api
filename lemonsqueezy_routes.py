from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/subscribe")
def subscribe():
    checkout_url = "https://thecoffeeshop.lemonsqueezy.com/checkout/product_id"  # Replace 'product_id' with your actual Lemon Squeezy product checkout path
    return RedirectResponse(url=checkout_url)
