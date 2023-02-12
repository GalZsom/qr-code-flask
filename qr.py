from flask import Flask, request, Response
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/qrcode', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return Response(buffer, content_type='image/jpeg', headers={
        'Content-Disposition': 'attachment; filename=qrcode.jpeg'
    })

if __name__ == '__main__':
    app.run(debug=True)