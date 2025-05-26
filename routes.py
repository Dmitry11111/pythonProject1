##создаем маршруты
from flask import Flask, request, render_template, url_for, redirect
from pythonProject1.models import ToDo, db


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # определяем систему управления баз данных
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	# инициализируем базу данных
	db.init_app(app)
	return app


# для работы с обьектом мы его вызовем и ниже будем писать маршруты
app = create_app()


# маршрут добавления
# маршрут обновления
# маршрут удаления
# crud функционал

@app.get('/')
def home():
	todo_list = ToDo.query.all()
	return render_template('todo/index.html', todo_list=todo_list, title='Главная страница')


# используем метод post для добавление записи
@app.post('/add')
def add():
	# забираем информацию из поля title с помощью get
	title = request.form.get('title')
	# new_todo мы делаем для того чтобы в title передавать title
	new_todo = ToDo(title=title, is_complete=False)
	# добавим в бд  спомощью добавления новой сесии
	db.session.add(new_todo)
	db.session.commit()
	return redirect(url_for('home'))  # когда нажимаем кнопку добавить то редирект переход на home - главную страницу


@app.get('/update/<int:todo_id>')  # id задания для обновления
def update(todo_id):  # функция update будет работать с методом get
	todo = ToDo.query.filter_by(id=todo_id).first()  # first - тк ищем единственный обьект
	# тodo это обьект который мы ищем при обновлении задачи
	# c помощью фильтра filter_by мы ищем идишник, который передаем в маршруте
	todo.is_complete = not todo.is_complete  # изначально iscomplete -false (не завершено) , при каждом нажатии на кнопку меняетсяtry false.....
	db.session.commit()  # отправляем изменения в базу данных
	return redirect(url_for('home'))


@app.get('/delete/<int:todo_id>')  # работаем с методом гет тк только удаляем записи а не отправляем
def delete(todo_id):
	todo = ToDo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for('home'))
