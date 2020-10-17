from codernitydb3.database_safe_shared import SafeDatabase
from codernitydb3.env import cdb_environment

try:
    from gevent.lock import RLock
except ImportError:
    raise NotImplementedError

cdb_environment["mode"] = "gevent"
cdb_environment["rlock_obj"] = RLock


class GeventDatabase(SafeDatabase):
    pass
