from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Halo import HaloTickets
from Crm import CrmTickets
from datetime import datetime
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)



# app.config.from_object(Config)
ht = HaloTickets()
ct = CrmTickets(db)


@app.route('/Tickets', methods=['GET'])
def getListTickets():
    tickets_list = ht.getTickets()
    return tickets_list


@app.route('/get-halo-tickets', methods=['GET'])
def test_get_tickets():
    return ht.getTickets()


@app.route('/get-halo-ticket/<ticket_id>', methods=['GET'])
def test_get_ticket(ticket_id):
    return ht.getTicket(ticket_id)


@app.route('/set-halo-ticket', methods=['GET'])
def test_post_ticket():
    return ht.postTicket(data={'summary': 'sum' + str(datetime),
                               'details': 'details'})


@app.route('/exportTickets', methods=['GET'])
def export_tickets():
    internal_tickets_list = ct.getTickets()
    # Данная функция находится в классе в файле Crm
    return ht.updateTickets(internal_tickets_list)


if __name__ == '__main__':
    app.run()