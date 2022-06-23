from flask_sqlalchemy import SQLAlchemy


class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    info = db.Column(db.String(800), nullable=False)
    __tablename__ = "tickets"

    user_id = db.Column (db.Integer, db.ForeignKey('Customers.id'))

    def __repr__(self):
        return f"Ticket {self.id}"


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    email = db.Column(db.String(80), unique=True)
    psw = db.Column(db.String(80))

    def __repr__(self):
        return f"Customer {self.id}"