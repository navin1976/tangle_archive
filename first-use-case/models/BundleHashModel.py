from cassandra.cqlengine import columns

from models.base import Base


class BundleHashModel(Base):
    __table_name__ = "bundle_hash_table"
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

