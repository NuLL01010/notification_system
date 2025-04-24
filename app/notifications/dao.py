from app.notifications.models import Notification
from sqlalchemy import update, insert
from app.database import async_session_maker, sync_session_maker


class NotificationDAO():
	model = Notification

	@classmethod
	def update_status(cls, task_id: int, new_status: str):
		with sync_session_maker() as session:
			stmt = (
				update(cls.model)
				.where(cls.model.id == task_id)
				.values(status=new_status)
			)
			session.execute(stmt)
			session.commit()

			
	
	@classmethod
	async def add(cls, **data):
		async with async_session_maker() as session:
			query = insert(cls.model).values(**data).returning(cls.model.id)
			
			result = await session.execute(query)
			
			task_id = result.scalar()  
			await session.commit()
			
			return task_id