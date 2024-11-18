import segno

# URL do site
url = "https://tribodenaftaly.netlify.app/"

# Gerar QR Code
qr = segno.make(url)

# Salvar o QR Code como imagem
qr.save("qrcode.png", scale=10)

