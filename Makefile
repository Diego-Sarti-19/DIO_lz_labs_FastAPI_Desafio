run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$$PYTHONPATH:$(PWD) alembic revision --autogenerate -m "$(d)"

run-migrations:
	@PYTHONPATH=$$PYTHONPATH:$(PWD) alembic upgrade head