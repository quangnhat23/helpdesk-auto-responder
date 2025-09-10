import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.text import MIMEText

#----------------------------------------
#	CONFIGURATION
#----------------------------------------

#For Outlook: outlook.office365.com
IMAP_SERVER = "imap.gmail.com" 
#For Outlook: smtp.office365.com
SMTP_SERVER ="smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ACCOUNT = "nguyennhatq22@gmail.com" #<---- change this
EMAIL_PASSWORD ="Allyouneediskill21" \
"" 	#<--- use App Password if 2FA enabled

#----------------------------------------
# SEND AUTO_REPLY
#----------------------------------------

def send_auto_reply (to_email, subject):
	reply_subject= f"Re: {subject}"
	reply_body ="""Hello, 

We've received your support request.Our team will get back to you shortly.

Thank you,
IT Support Team
"""
	msg = MIMEText(reply_body)
	msg["From"] = EMAIL_ACCOUNT
	msg["To"] = to_email
	msg["Suject"] = reply_subject
	
	try:
		with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
			server.starttls()
			server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
			server.sendmail(EMAIL_ACCOUNT, to_email,msg.as_string())
		print(f"[OK] Auto_reply sent to {email}")
	except Exception as e:
		print(f"[ERROR] Failed to send email: {e}")
#----------------------------
#TESTING
#----------------------------
if __name__=="__main__":
    test_email = input("Enter a recipient email to send a test reply: ")
    send_auto_reply(test_email, "Test Ticket")
