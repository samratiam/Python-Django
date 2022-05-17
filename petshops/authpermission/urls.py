from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView,TokenVerifyView

from .views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
# from .views import MyObtainTokenPairView

# from django_rest_passwordreset.views import ResetPasswordValidateTokenViewSet, ResetPasswordConfirmViewSet, 
#     ResetPasswordRequestTokenViewSet

router = DefaultRouter()
router.register(r'locations',LocationModelViewSet,basename='location')
router.register(r'petstores',PetstoreModelViewSet,basename='petstore')
router.register(r'categories',CategoryModelViewSet,basename='category')
router.register(r'breeds',BreedModelViewSet,basename='breed')
router.register(r'employees',EmployeeModelViewSet,basename='employee')
router.register(r'customers',CustomerModelViewSet,basename='customer')
router.register(r'sales',SaleModelViewSet,basename='sale')
router.register(r'register',RegistrationView,basename='register'),
# router.register(r'resetpassword',include('django_rest_passwordreset.urls'),basename='resetpassword')
# router.register(r'password_reset',RequestPasswordResetEmail,basename='resetemail'),
# router.register(
#     r'passwordreset/validate_token',
#     ResetPasswordValidateTokenViewSet,
#     basename='reset-password-validate'
# )
# router.register(
#     r'passwordreset/confirm',
#     ResetPasswordConfirmViewSet,
#     basename='reset-password-confirm'
# )
# router.register(
#     r'passwordreset/',
#     ResetPasswordRequestTokenViewSet,
#     basename='reset-password-request'
# )

urlpatterns = [
    path('gettoken/',MyObtainTokenPairView.as_view(),name='token_obtain_pair'), #both access and refresh token
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),  #get new refresh token
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'), #Optional to check validation of the token
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
    
]