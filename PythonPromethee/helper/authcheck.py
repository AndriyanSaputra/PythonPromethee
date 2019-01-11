# from orm.models import Pekerja

# class AuthCheck:

#     @staticmethod
#     def isSuperUser(user):
#         if user.is_superuser:
#             return True
#         else:
#             return False
#     @staticmethod
#     def isPekerja(user):
#         if user.is_staff:
#             try:
#                 user.pekerja
#                 return True
#             except Pekerja.DoesNotExist:
#                 return False
#         else:
#             return False
    