import os
import uuid

id1 = uuid.uuid1()
id2 = uuid.UUID(bytes=os.urandom(16), version=1)
id3 = uuid.UUID(None, b'1234567891234567', None, None, None, 1)