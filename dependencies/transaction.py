import threading

class TransactionManager(object):

    def __init__(self):
        pass

    def begin(self):
        """ See ITransactionManager.
        """
        pass

    def get(self):
        """ See ITransactionManager.
        """
        pass

    def free(self, txn):
        pass

    def registerSynch(self, synch):
        """ See ITransactionManager.
        """
        pass

    def unregisterSynch(self, synch):
        """ See ITransactionManager.
        """
        pass

    def isDoomed(self):
        """ See ITransactionManager.
        """
        pass

    def doom(self):
        """ See ITransactionManager.
        """
        pass

    def commit(self):
        """ See ITransactionManager.
        """
        pass

    def abort(self):
        """ See ITransactionManager.
        """
        pass

    def __exit__(self, t, v, tb):
        pass

    def savepoint(self, optimistic=False):
        """ See ITransactionManager.
        """
        pass

    def attempts(self, number=3):
        pass

    def _retryable(self, error_type, error):
        pass


class ThreadTransactionManager(TransactionManager, threading.local):
    """Thread-aware transaction manager.
    Each thread is associated with a unique transaction.
    """
    pass

manager = ThreadTransactionManager()
get = __enter__ = manager.get
begin = manager.begin
commit = manager.commit
abort = manager.abort
__exit__ = manager.__exit__
doom = manager.doom
isDoomed = manager.isDoomed
savepoint = manager.savepoint
attempts = manager.attempts