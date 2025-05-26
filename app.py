from pythonProject1.routes import app, db

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.run()
		app.run(debug=True, port=5555)
