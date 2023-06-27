import base64
from io import BytesIO
import pyqrcode


class QRcode:
    qr_str = ""

    @classmethod
    def validate(cls, arg):
        if type(arg) == str:
            return True
        else:
            print(f'Something wrong - {arg}. It is not a string')

    def __init__(self):
        pass

    def get_qr_code(self, qr_str):
        try:
            data = qr_str
            c = pyqrcode.create(data)
            s = BytesIO()
            c.png(s, scale=6)
            image_bytes = s.getvalue()
            base64_data = self.__get_base64(image_bytes)

            return base64_data

        except:
            print("Something goes wrong")

    def __get_base64(self, image_bytes):
        base64_data = base64.b64encode(image_bytes).decode("utf-8")
        return base64_data
