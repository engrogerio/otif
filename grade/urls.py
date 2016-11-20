

from django.conf.urls import url
from views import GradeListView

urlpatterns = [
    #url(r'^grade/(?P<id>\d+)/$', GradeDetailView.as_view(), name='grade_detail' ),
    url(r'$', GradeListView.as_view(), name='grade_list' ),
]