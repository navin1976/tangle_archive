import datetime
import os
import transaction
from schema import Transaction, Address, Tag,\
    Bundle, Approvee, TransactionObject, KEYSPACE
from cassandra.cqlengine.management import sync_table, sync_type
from cassandra.cqlengine import connection
from cassandra.cqlengine.query import LWTException


folder = './'


def create_connection():
    connection.setup(['127.0.0.1'], 'cqlengine', protocol_version=3)


def sync_tables():
    sync_table(Transaction)
    sync_table(Address)
    sync_table(Tag)
    sync_table(Bundle)
    sync_table(Approvee)

def sync_types():
    sync_type(KEYSPACE, TransactionObject)

class Store:
    def __init__(self):
        self.extract_dump()

    def extract_dump(self):
        for file in sorted(os.listdir(folder)):
            if file.endswith('.dmp'):
                count = 0
                with open(folder + file, 'r') as f:
                    for line in f:
                        tx_hash, tx = line.split(',')
                        tx = transaction.transaction(tx, tx_hash)

                        hash = tx.hash
                        branch = tx.branch_transaction_hash
                        trunk = tx.trunk_transaction_hash

                        Transaction.create(tx)
                        Address.create_or_update(tx.address, hash)
                        Tag.create_or_update(tx.tag, hash)
                        Bundle.create_or_update(tx.bundle_hash, hash)
                        Approvee.create_or_update(branch, hash)
                        Approvee.create_or_update(trunk, hash)

                        count += 1
                        print 'Dumped so far', count


if __name__ == '__main__':
    create_connection()
    sync_tables()
    sync_types()
    Store()
