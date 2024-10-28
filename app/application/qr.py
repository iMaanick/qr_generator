import base64
import io

import qrcode


async def generate_qr_code(url: str) -> str:
    """
    Generates a QR code and returns it in base64 format.
    """
    qr = qrcode.make(url)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    base64_img = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{base64_img}"
