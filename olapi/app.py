from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Crm import crm_tickets
from Halo import halo_tickets
from datetime import datetime

#from config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
#app.config.from_object(Config)
ht = halo_tickets()
ct = crm_tickets()


@app.route('/Tickets', methods=['GET'])
def getListTickets():
    tickets_list = ht.getTickets()
    return tickets_list

@app.route('/get-halo-tickets', methods=['GET'])
def test_get_tickets():
    return ht.getTickets()

@app.route('/set-halo-ticket', methods=['GET'])
def test_post_ticket():
    return ht.postTicket(data={'summary': 'sum' + str(datetime),
                               'details': 'detals'})

@app.route('/exportTickets', methods=['GET'])
def export_tickets():
    internal_tickets_list = crm.getTickets()
    # Данная функция находится в классе в файле Crm
    return halo.updateTickets(internal_tickets_list)


if __name__ == '__main__':
    app.run()
