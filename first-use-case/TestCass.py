from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask

from models.Transactions import TransactionModel
from views.api import api

KEYSPACE = "snapshots"


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)

    cluster = Cluster()
    session = cluster.connect()

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)

    session = cluster.connect(keyspace=KEYSPACE)


    return app


app = create_app()

if __name__ == '__main__':
    connection.setup(['127.0.0.1'] ,"cqlengine", protocol_version=3)
    sync_table(TransactionModel)
    app.run(debug=True)