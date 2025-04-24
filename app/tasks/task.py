from celery import Celery
from app.config import settings


celery_app = Celery(
	main="task",
	broker=f"{settings.BROKER}://{settings.BROKER_URL}" 
)


celery_app.conf.update(
    result_backend=f"{settings.BROKER}://{settings.BROKER_URL}",  
)

celery_app.config_from_object("app.config.settings", namespace="CELERY")
celery_app.autodiscover_tasks(["app.notifications.services"])