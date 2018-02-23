from cassandra.cqlengine import columns
from permanode import db
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType

class Base(db.Model):
    __abstract__ = True
    __keyspace__ = "permanode"


class TransactionObject(UserType):
    hash = columns.Text()

    def as_json(self):
        return {
            "hash": self.hash
        }

class Transaction(Base):
    __table_name__ = "transactions"

    hash_ = columns.Text(primary_key=True)
    address = columns.Text()
    value = columns.BigInt()
    transaction_time = columns.Integer()
    signature_message_fragment = columns.Text()
    tag = columns.Text()
    tag_index = columns.BigInt()
    current_index = columns.Integer()
    last_index = columns.Integer()
    bundle = columns.Text()
    trunk_transaction_hash = columns.Text()
    branch_transaction_hash = columns.Text()
    nonce = columns.Text()
    min_weight_magnitude = columns.Integer()

    def as_json(self):
        return {
            "address": self.address,
            "value": self.value,
            "timestamp": self.transaction_time,
            "hash": self.hash_,
            "signature_message_fragment": self.signature_message_fragment,
            "tag": self.tag,
            "tag_index": self.tag_index,
            "current_index": self.current_index,
            "last_index": self.last_index,
            "bundle": self.bundle,
            "trunk_transaction_hash": self.trunk_transaction_hash,
            "branch_transaction_hash": self.branch_transaction_hash,
            "nonce": self.nonce,
            "min_weight_magnitude": self.min_weight_magnitude,
            "persistence": True  # since all txs from db are confirmed
        }

class Bundle(Base):
    __table_name__ = 'bundles'

    bundle = columns.Text(primary_key=True, required=True)
    transactions = columns.List(columns.UserDefinedType(TransactionObject))

    def as_json(self):
        return {
            "bundle": self.bundle,
            "transactions": self.transactions
        }


class Tag(Base):
    __table_name__ = 'tags'


    tag = columns.Text(primary_key=True, required=True)
    transactions = columns.List(columns.UserDefinedType(TransactionObject))

    def as_json(self):
        return {
            "tag": self.tag,
            "transactions": self.transactions

        }


class Address(Base):
    __table_name__ = 'addresses'

    address = columns.Text(primary_key=True, required=True)
    transactions = columns.List(columns.UserDefinedType(TransactionObject))

    @classmethod
    def get(cls, address):
        return Address.objects.get(address=address)

    def as_json(self):
        return {
            "address": self.address,
            "transactions": self.transactions
        }

class Approvee(Base):
    __table_name__ = 'approvees'

    hash = columns.Text(primary_key=True, required=True)
    approvees = columns.List(columns.UserDefinedType(TransactionObject))

    def as_json(self):
        return {
            "hash": self.hash,
            "approvees": self.approvees
        }