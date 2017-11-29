from cassandra.cqlengine import columns

from models.base import Base


class TransactionModel(Base):
   # __table_name__ = "transactions"
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

