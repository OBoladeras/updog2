import io
import socket
import qrcode
import base64
import webbrowser


def show(port: int, ssl: bool) -> None:
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

    webbrowser.open(f"data:image/png;base64,{base64_image}")
