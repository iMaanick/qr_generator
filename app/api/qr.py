from dataclasses import dataclass

from fastapi import APIRouter, Query

from app.application.qr import generate_qr_code

qr_router = APIRouter()


@dataclass
class QRResult:
    url: str
    qr_code: str


@qr_router.get("/", response_model=QRResult)
async def get_qr_code(
        url: str = Query("https://renident.ru/")
) -> QRResult:
    """
    Generates a QR code for the specified URL.

    Parameters:
    - url (str): The URL for which to generate the QR code. Defaults to
      "https://renident.ru/".

    Returns:
    - QRResult: An object containing the URL and the generated QR code.
    """
    qr_code = await generate_qr_code(url)
    res = QRResult(url=url, qr_code=qr_code)
    return res
