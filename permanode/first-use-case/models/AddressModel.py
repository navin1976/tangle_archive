from cassandra.cqlengine import columns

from models.base import Base


class AddressModel(Base):
    __table_name__ = "address_table"
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

