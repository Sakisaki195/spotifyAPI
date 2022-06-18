from django.urls import path
from . import views # 同じ階層内のviews.pyを読み込んでる

app_name = 'helloworld'
urlpatterns = [
    path('', views.index, name='index') # URLに何も付いてなければviews.pyのindex関数を実行する
]