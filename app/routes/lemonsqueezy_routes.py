from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/subscribe")
def subscribe():
    checkout_url = "https://thecoffeeshop.lemonsqueezy.com/checkout/product_id"
    return RedirectResponse(url=checkout_url)
