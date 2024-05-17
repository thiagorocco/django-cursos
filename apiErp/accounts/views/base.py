from rest_framework import APIView
from companies.models import Enterprise


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