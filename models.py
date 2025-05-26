#создаем базу данных
from flask_sqlalchemy import SQLAlchemy

#создадим объект
db = SQLAlchemy()
#создаем класс для базы данных id, title-тестовое поле куда записываем задачу
#is_complete - галочка переключатель завершено-закрыть
class ToDo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(500))
	is_complete = db.Column(db.Boolean)