from ridemyway.api.authentication.models import User
from ridemyway.api.authentication.serializer import UserSerializer
from ..utilities.base_classes.views import BaseModelView, BaseSingleModelView


class UserView(BaseModelView):
    """ Generic view for creating and listing all users """

    queryset = User.objects.filter().all()
    serializer_class = UserSerializer
    model_name = 'User'


class SingleUserView(BaseSingleModelView):
    """ Generic view for retrieving, updating and deleting a user """
    
    queryset = User.objects.filter().all()
    serializer_class = UserSerializer
    model_name = 'User'
