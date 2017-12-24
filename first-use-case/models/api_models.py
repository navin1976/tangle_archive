from cassandra.cqlengine import columns
from base import Base

class AddressModel(Base):
    __table_name__ = "table_address_info"
    address = columns.Text(primary_key=True)
    value = columns.BigInt(primary_key=True)
    timestamp_int = columns.Integer(primary_key=True)
    hash = columns.Text(primary_key=True)

    def get_address_data(self):
        return {
            "hash": self.hash,
            "address": self.address,
            "value": str(self.value),
            "timestamp_int": str(self.timestamp_int)
        }

class AddressTokenReceivedModel(Base):
    __table_name__ = "table_tokens_revieved_by_address"
    address = columns.Text(primary_key=True)
    total_tokens_received = columns.Counter()

    def get_data(self):
        return {
            "total_tokens_received": self.total_tokens_received
        }

class BundleHashModel(Base):
    __table_name__ = "table_bundle_search"
    bundle_hash = columns.Text(primary_key=True)
    hash = columns.Text(primary_key=True);
    address = columns.Text(index=True)
    value = columns.BigInt()
    current_index = columns.Integer()
    last_index = columns.Integer()
    timestamp_int = columns.Integer(index=True)


    def get_bundle_data(self):
        return {
            "hash": self.hash,
            "address": self.address,
            "value": self.value,
            "timestamp_int": str(self.timestamp_int),
            "current_index": str(self.current_index),
            "last_index": str(self.last_index),
            "bundle_hash": self.bundle_hash
        }

class DateModel(Base):
    __table_name__ = "date_table"
    date = columns.Text(primary_key=True)
    count = columns.Counter()

    def get_date_count(self):
        return {
            "date": self.date,
            "Number of transections": str(self.count)
        }

from models.base import Base


class TagModel(Base):
    __table_name__ = "tag_table"
    tag = columns.Text(primary_key=True)
    address = columns.Text(primary_key=True)
    hash = columns.Text(primary_key=True)
    tagIndex = columns.BigInt()
    signature_message_fragment = columns.Text()


    def get_tag_data(self):
        return {
            "hash": self.hash,
            "signature_message_format": self.signature_message_fragment,
            "address": self.address,
            "tag": str(self.tag),
            "tagIndex": str(self.tagIndex)
        }

class TransactionModel(Base):
    __table_name__ = "transactions"
   # __keyspace__ = "snapshots"
    hash = columns.Text(primary_key=True);
    signature_message_fragment = columns.Text()
    address = columns.Text(index=True)
    value = columns.BigInt()
    tag = columns.Text(index=True)
    tagIndex = columns.BigInt()
    timestamp_int = columns.Integer(index=True)
    current_index = columns.Integer()
    last_index = columns.Integer()
    bundle_hash = columns.Text(index=True)
    trunk_transaction_hash = columns.Text()
    branch_transaction_hash = columns.Text()
    nonce = columns.Text()


    def get_transaction_data(self):
        return {
            "hash": self.hash,
            "signature_message_format": self.signature_message_fragment,
            "address": self.address,
            "value": self.value,
            "tag": str(self.tag),
            "tagIndex": str(self.tagIndex),
            "timestamp_int": str(self.timestamp_int),
            "current_index": str(self.current_index),
            "last_index": str(self.last_index),
            "bundle_hash": self.bundle_hash,
            "trunk_transaction_hash": self.trunk_transaction_hash,
            "branch_transaction_hash": self.branch_transaction_hash,
            "nonce": self.nonce
        }
