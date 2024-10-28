from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.application.qr import generate_qr_code

index_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@index_router.get("/", response_class=HTMLResponse)
async def index(
        request: Request,
) -> HTMLResponse:
    """
    Renders the main page displaying a QR code with a default URL.
    """
    default_url = "https://renident.ru/"
    qr_code = await generate_qr_code(default_url)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "url": default_url,
            "qr_code": qr_code
        }
    )
