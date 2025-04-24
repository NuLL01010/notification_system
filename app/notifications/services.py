import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.notifications.dao import NotificationDAO
from app.tasks.task import celery_app


@celery_app.task
def send_simple_email(task_id, sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password):
    try:
        NotificationDAO.update_status(int(task_id), "success")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        return {"id": int(task_id), "status": "success"}

    except Exception as e:
        NotificationDAO.update_status(int(task_id), "field")
        return {"id": int(task_id), "status": "field"}

    

