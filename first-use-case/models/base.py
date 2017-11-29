from cassandra.cqlengine.models import Model


class Base(Model):
    __abstract__ = True
    __table_name__ = "transactions"
    __keyspace__ = "snapshots"

