"""smspy - send sms via python using gmail -
   Usage: smspy('email', 'password', 'phone_number', 'carrier', 'message'
   Current Carrier Support: Att, Verizon,"""
import smtplib
def sms(email,password,number,carrier,txt):
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mailserver.ehlo()
    mailserver.login(email,password)
    carrier = carrier.lower()
    if carrier == 'att':
        number = number + '@text.att.net'
    if carrier == 'verizon':
        number = number + '@vtext.com'
    mailserver.sendmail(email, number, txt)        



