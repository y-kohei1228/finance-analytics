from django.shortcuts import render

# Create your views here.
# 以下を全て追加(4-2 Djangoでのページ追加の手順)
from django.views import generic
# DetailViewを追加（7-2 ナビゲーションバーの編集）
from django.views.generic import TemplateView, DetailView
from .models import Company, Fstatement  # この行を追加（5-4 トップページでの表示）
# この行を追加(10-3 ページネーションとは)
from django.views.generic.list import MultipleObjectMixin


class IndexView(TemplateView):  # クラス名を変更（5-4 トップページでの表示）
    template_name = 'finchart/index.html'

    # ========以下すべて追加（5-4 トップページでの表示）========
    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params


# CompanyViewを変更(10-3 ページネーションとは)
# ========以下をすべて追加(7-2 ナビゲーションバーの編集)========
class CompanyView(DetailView, MultipleObjectMixin):
    model = Company
    paginate_by = 4

    def get_context_data(self, **kwargs):
        object_list = Fstatement.objects.filter(
            company=kwargs['object']).order_by('-fiscal_year')
        context = super(CompanyView, self).get_context_data(
            object_list=object_list, **kwargs)

        return context

# ========以下をすべて追加(8-2 決算詳細ページを表示するための準備をする)========


class FstatementView(DetailView):
    model = Fstatement
