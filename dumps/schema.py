from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType
from cassandra.cqlengine.query import LWTException

KEYSPACE = 'permanode'

class Base(Model):
    __abstract__ = True
    __keyspace__ = KEYSPACE


class TransactionAlreadyExistsException(Exception): pass


class TransactionObject(UserType):
    hash = columns.Text()

    def as_json(self):
        return {
            "hash": self.hash,
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
            "hash": self.hash,
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

    @classmethod
    def get(cls, hash):
        return Transaction.objects.get(hash=hash)

    @classmethod
    def create(cls, tx):
        try:
            return Transaction.if_not_exists().create(
                hash_=tx.hash,
                address=tx.address,
                value=tx.value,
                transaction_time=tx.timestamp,
                signature_message_fragment=tx.signature_message_fragment,
                tag=tx.tag,
                tag_index=tx.tagIndex,
                current_index=tx.current_index,
                last_index=tx.last_index,
                bundle=tx.bundle_hash,
                trunk_transaction_hash=tx.trunk_transaction_hash,
                branch_transaction_hash=tx.branch_transaction_hash,
                nonce=tx.nonce,
                min_weight_magnitude=tx.min_weight_magnitude
            )

        except LWTException as e:
            raise TransactionAlreadyExistsException()


class Bundle(Base):
    __table_name__ = 'bundles'

    bundle = columns.Text(primary_key=True, required=True)
    transactions = columns.List(columns.UserDefinedType(TransactionObject))

    @classmethod
    def create_or_update(cls, bundle, hash):
        try:
            return Bundle.if_not_exists().create(
                bundle=bundle,
                transactions=[
                    TransactionObject(
                        hash=hash
                )]
            )
        except LWTException:
            pass
        try:
            return Bundle.objects(bundle=bundle).update(
                transactions__append=[
                    TransactionObject(
                        hash=hash
                )]
            )
        except LWTException:
            raise Exception('Could not update bundle.')

    def as_json(self):
        return {
            "bundle": self.bundle,
            "transactions": self.transactions
        }


class Tag(Base):
    __table_name__ = 'tags'


    tag = columns.Text(primary_key=True, required=True)
    transactions = columns.List(columns.UserDefinedType(TransactionObject))

    @classmethod
    def create_or_update(cls, tag, hash):
        try:
            return Tag.if_not_exists().create(
                tag=tag,
                transactions=[
                    TransactionObject(
                        hash=hash
                    )]
            )
        except LWTException:
            pass
        try:
            return Tag.objects(tag=tag).update(
                transactions__append=[
                    TransactionObject(
                        hash=hash
                    )]
            )
        except LWTException:
            raise Exception('Could not update tag.')

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
    def create_or_update(cls, address, hash):
        try:
            return Address.if_not_exists().create(
                address=address,
                transactions=[
                    TransactionObject(
                        hash=hash
                    )]
            )
        except LWTException:
            pass
        try:
            return Address.objects(address=address).update(
                transactions__append=[
                    TransactionObject(
                        hash=hash
                    )]
            )
        except LWTException:
            raise Exception('Could not update address.')

    def as_json(self):
        return {
            "address": self.address,
            "transactions": self.transactions
        }

class Approvee(Base):
    __table_name__ = 'approvees'

    hash = columns.Text(primary_key=True, required=True)
    approvees = columns.List(columns.UserDefinedType(TransactionObject))

    @classmethod
    def create_or_update(cls, reference, hash):
        try:
            return Approvee.if_not_exists().create(
                hash=reference,
                approvees=[
                    TransactionObject(
                        hash=hash
                )]
            )
        except LWTException:
            pass
        try:
            return Approvee.objects(hash=reference).update(
                approvees__append=[
                    TransactionObject(
                        hash=hash
                )]
            )
        except LWTException:
            raise Exception('Could not update approvee.')

    def as_json(self):
        return {
            "hash": self.hash,
            "approvees": self.approvees
        }