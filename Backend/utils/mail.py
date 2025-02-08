from instance.mail import mail
from flask_mail import Message
from instance.app import app

def send_email(receiver_email, subject, body, attachment=None, attachment_type=None, mime_type="application/pdf"):  
    try:
        msg = Message(subject, recipients=[receiver_email],body = body)
        if attachment:
            with app.open_resource(attachment) as file:
                if mime_type == 'application/pdf':
                    msg.attach("report.pdf", mime_type, file.read())
                elif mime_type == 'application/x-zip':
                    msg.attach("report.zip", mime_type, file.read())
                elif mime_type == 'text/csv':
                    msg.attach("data.csv", mime_type, file.read())
        mail.send(msg)
        return "Mail sent successfully"
    except Exception as e:
        print(e)
        
# def mass_email(receiver_emails, subject, body, attachment=None, attachment_type=None):  
#     try:
#         msg = Message(subject, recipients=receiver_emails,body = body)
#         mail.send(msg)
#         return "Mail sent successfully"
#     except Exception as e:
#         print(e) 

# def html_mail(receiver_email, subject, body_content_html, attachment=None, attachment_type=None, mime_type="application/pdf"):  
#     try:
#         msg = Message(subject, recipients=[receiver_email],html = body_content_html)
#         if attachment:
#             with app.open_resource(attachment) as file:
#                 if mime_type == 'application/pdf':
#                     msg.attach("report.pdf", mime_type, file.read())
#                 elif mime_type == 'application/x-zip':
#                     msg.attach("report.zip", mime_type, file.read())
#                 elif mime_type == 'text/csv':
#                     msg.attach("data.csv", mime_type, file.read())
#         mail.send(msg)
#         return "Mail sent successfully"
#     except Exception as e:
#         print(e)