from cassandra.cqlengine import columns

from models.base import Base


class AddressModel(Base):
    __table_name__ = "search_by_address"
    address = columns.Text(primary_key=True)
    timestamp_int = columns.Integer(primary_key=True, clustering_order="DESC")
    hash = columns.Text(primary_key=True)
    value = columns.BigInt()

    def get_address_data(self):
        return {
            "hash": self.hash,
            "address": self.address,
            "value": str(self.value),
            "timestamp_int": str(self.timestamp_int)
        }

