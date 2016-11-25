

from django.conf.urls import url
from views import GradeListView, GradeDetailView

urlpatterns = [
    url(r'^$', GradeListView.as_view(), name='grade_list'),
    url(r'^(?P<pk>\d+)/$', GradeDetailView.as_view(), name='grade_detail' ),

]