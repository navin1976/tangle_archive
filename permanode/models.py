from cassandra.cqlengine import columns
from permanode import db


class Base(db.Model):
    __abstract__ = True
    __keyspace__ = "snapshotsdb"


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

    def get_transaction_token_received_data(self):
        return {
            "total_tokens_received": self.total_tokens_received
        }


class BundleHashModel(Base):
    __table_name__ = "table_bundle_search"
    bundle_hash = columns.Text(primary_key=True)
    hash = columns.Text(primary_key=True)
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


class TagModel(Base):
    __table_name__ = "table_tag_search"
    tag = columns.Text(primary_key=True)
    timestamp_int=columns.Integer(primary_key=True, clustering_order='DESC')
    address = columns.Text(primary_key=True)
    hash = columns.Text(primary_key=True)
    tagIndex = columns.BigInt()
    signature_message_fragment = columns.Text()

    def get_tag_data(self):
        return {
            "tag": self.tag,
            "address":self.address,
            "timestamp_int": self.timestamp_int,
            "hash": self.hash,
            "tag_index": self.tagIndex,
            "signature_massage_fragment": self.signature_message_fragment
            # tag = trans.tag,
            # timestamp_int=trans.timestamp,
            # address = trans.address,
            # hash = trans.hash,
            # tagIndex = trans.tagIndex,
            # signature_message_fragment = trans.signature_message_fragment
        }


class TransactionModel(Base):
    __table_name__ = "transactions"
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
class TransactionApproveeModel(Base):
    __table_name__ = "table_transaction_approvee"
    hash = columns.Text(primary_key=True)
    approvee_hash = columns.Text(primary_key=True)

    def get_transaction_approvee_data(self):
        return {
            "hash": self.hash,
            "approvee_hash":self.approvee_hash
        }

