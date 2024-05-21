from rest_framework import APIView
from rest_framework.exceptions import APIException
from companies.models import Enterprise, Employee
from accounts.models import User_Groups, Group_Permissions


class Base(APIView):
    # Obter uma empresa baseado em um usuário
    def get_entrerprise_user(self, user_id) -> dict[str, Any] | None:
        enterprise = {
            "is_owner": False,
            "permissions": []
        }
        enterprise['is_owner'] = Enterprise.objects.filter(
            user_id=user_id).exists()
        # Se for dono já retorna a empresa, pois já possui todas as permissões
        if enterprise['is_owner']:
            return enterprise    
        # Permissions, Get Employee
        employee = Employee.objects.filter(user_id=user_id).first()
        if not employee:
            raise APIException("Este usuário não é um funcionário")

        groups = User_Groups.objects.filter(user_id=user_id).all()

        for g in groups:
            group = g.group
            permissions = Group_Permissions.objects.filter(
                group_id=group.id).all()
            for p in permissions:
                enterprise['permissions'].append({
                    "id": p.permission.id,
                    "label": p.permission.name,
                    "codename": p.permission.codename
                })
        return enterprise
