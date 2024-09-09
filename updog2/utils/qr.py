import io
import socket
import qrcode
import base64
import webbrowser


def generate(port: int, ssl: bool) -> str:
    r"""
    Generate a QR code image with the link to the server.  
    :param port: The port the server is running on.  
    :param ssl: Whether the server is running with SSL.  
    :return: A base64 encoded image

    Example:
    >>> generate(8080, False)
    """

    def get_ip_address() -> str:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(('8.8.8.8', 80))
                local_ip = s.getsockname()[0]
        except Exception as e:
            local_ip = str(e)

        return local_ip

    link = "http"
    link += ("://" if not ssl else "s://") + f"{get_ip_address()}:{port}"

    qrimage = qrcode.make(link)

    bitMap = io.BytesIO()
    qrimage.save(bitMap)
    bitMap.seek(0)
    base64_image = base64.b64encode(bitMap.getvalue()).decode('utf-8')

    return f"data:image/png;base64,{base64_image}"


def show(port: int, ssl: bool) -> None:
    r"Open the default web browser with the QR code image."

    webbrowser.open(generate(port, ssl))
