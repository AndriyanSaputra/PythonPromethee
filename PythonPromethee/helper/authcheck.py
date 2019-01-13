
from orm.models import Pemilih

class AuthCheck:
    @staticmethod
    def isSuperUser(user):
        if user.is_superuser:
            return True
        else:
            return False
    @staticmethod
    def isPemilih(user):
        if user.is_staff:
            try:
                user.pemilih
                return True
            except Pemilih.DoesNotExist:
                return False
        else:
            return False