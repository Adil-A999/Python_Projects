import qrcode
#taking upi id as input
upi_id = input('Enter your UPI ID =')

google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonpe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create Qr codes for each payment app

phonpe_qr = qrcode.make(phonpe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

phonpe_qr.show()
paytm_qr.show()
google_pay_qr.show()