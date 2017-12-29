from cassandra.cqlengine import columns

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