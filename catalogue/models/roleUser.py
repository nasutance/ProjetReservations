from django.db import models
from .role import Role
from .user import User

class RoleUser(models.Model):
    role_user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "role_user"

    def __str__(self):
        return f'{self.role} - {self.user}'
