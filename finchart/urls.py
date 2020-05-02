from django.urls import path

from . import views

app_name = 'finchart'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # IndexTemplateViewからIndexViewに変更（5-4 トップページでの表示）
    path('company/<int:pk>', views.CompanyView.as_view(), name='company'), # これを追加（7-2 ナビゲーションバーの編集）
    path('fstatement_detail/<int:pk>', views.FstatementView.as_view(), name='fstatement'), # これを追加(8-2 決算詳細ページを表示するための準備をする)
]
