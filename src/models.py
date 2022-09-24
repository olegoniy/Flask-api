from app import db


class Tickets(db.Model):
	__tablename__ = "tickets"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), unique=True)
	info = db.Column(db.String(800), nullable=False)

	user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

	def __repr__(self):
		return "<Tickets {}>".format(self.id)


class Customers(db.Model):
	__tablename__ = "customers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(25), unique=True)
	email = db.Column(db.String(80), unique=True)
	psw = db.Column(db.String(80))

	def __repr__(self):
		return "<Customer {}>".format(self.id)
