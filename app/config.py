from environs import Env

class Settings:
	env = Env()
	env.read_env()

	DB_USER=env("DB_USER")
	DB_PASS=env('DB_PASS')
	DB_HOST=env('DB_HOST')
	DB_PORT=env('DB_PORT')
	DB_NAME=env('DB_NAME')

	BROKER = env('BROKER')
	BROKER_URL = env('BROKER_URL')

	SENDER_EMAIL = env('SENDER_EMAIL')
	LOGIN_EMAIL = env('LOGIN_EMAIL')
	PASSWORD_EMAIL = env('PASSWORD_EMAIL')
	SMTP_SERVER = env('SMTP_SERVER')
	SMTP_PORT = env('SMTP_PORT')



settings = Settings()