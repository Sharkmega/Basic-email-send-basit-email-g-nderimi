
from smtplib import SMTP

def gonder():

    try:
        subcjet = input("Lütfen konuyu yazınız: ")
        message = input("Lütfen mesajı yazınız: ")
        content = "Subject: {0}\n\n{1}".format(subcjet, message)

        # Hesap Bilgileri
        myMailAdress = input("Lütfen Mail adresinizi yazınız: ")
        password = input("Lütfen şifrenizi giriniz: ")

        # Kime Gönderilecek Bilgisi
        sendTo = input("Kime gönderilicek?: ")

        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
        print("Mail Gönderme İşlemi Başarılı!")
    except Exception as e:
        print("Hata Oluştu!\n {0}".format(e))

while True:
    gonder()