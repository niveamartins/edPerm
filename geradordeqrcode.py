import qrcode

class Gerador():

    def gerarQrcode(self,id,usuario):

        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 15,
            border = 4
        )

        qr.add_data(id)
        qr.make(fit=True)
        img = qr.make_image(fill = 'black', back_color = 'white')
        img.save('qrcodeDoUsuario{}.png'.format(usuario))
    
