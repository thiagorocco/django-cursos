from rest_framework import APIView
from rest_framework.exceptions import APIException
from companies.models import Enterprise, Employee


class Base(APIView):
    def get_entrerprise_user(self, user_id) -> dict[str, Any] | None:
        enterprise = {
            "is_owner": False,
            "permissions": []
        }
        enterprise['is_owner'] = Enterprise.objects.filter(
            user_id=user_id).exists()
        # Se for dono já retorna a empresa, pois um dono já possui todas as permissões
        if enterprise['is_owner']:
            return enterprise
    
        # Permissions, Get Employee
        employee = Employee.objects.filter(user_id=user_id).first()
        if not employee:
            raise APIException("Este usuário não é um funcionário")