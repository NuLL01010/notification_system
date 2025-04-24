from fastapi import APIRouter

from app.notifications.schemas import SEmailNotify, SSmsNotify
from app.notifications.dao import NotificationDAO
from app.notifications.services import send_simple_email
from app.config import settings

router = APIRouter( 
	prefix="/notifications",
	tags=["notifications"]
)



@router.post("/send/email")
async def send_email(data: SEmailNotify):
    task_id = await NotificationDAO.add(
        status = "queued", 
        task_type = "email",
        to = data.to,
        subject = data.subject,
        body = data.body, 
        error_message = data.error_message
    )
    res_status = send_simple_email.delay(
        task_id = task_id,
        sender_email=settings.SENDER_EMAIL,
        receiver_email=data.to,
        subject=data.subject,
        body=data.body,
        smtp_server=settings.SMTP_SERVER,
        smtp_port=settings.SMTP_PORT,
        login=settings.LOGIN_EMAIL,
        password=settings.PASSWORD_EMAIL
    )

    return {
        "id": task_id,
        "status": res_status.status
    }



@router.post("/send/sms")
async def send_sms(data: SSmsNotify):
    pass # сервисы по рассылке смс с апи послали меня нахуй