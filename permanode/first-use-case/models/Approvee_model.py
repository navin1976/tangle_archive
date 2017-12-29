from cassandra.cqlengine import columns

from models.base import Base

class ApproveeModel(Base):
    __table_name__ = "approvee_table"
    hash = columns.Text(primary_key=True)
    approvee_hash = columns.Text(primary_key=True)

    def get_approvee_hash(self):
        return {
            "hash": self.hash,
            "approvee_hash":self.approvee_hash
        }
