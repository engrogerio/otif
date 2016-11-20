from django.shortcuts import render
from django.views import generic
from grade.models import Grade
from django.http import Http404

# Create your views here.
class GradeListView(generic.ListView):
    template_name = 'grade_list.html'
    model = Grade

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(GradeListView, self).get_context_data(**kwargs)
            print(context)

            try:
                context['seg'] = Grade.objects.filter(dt_semana=0).order_by('hr_grade')
                context['ter'] = Grade.objects.filter(dt_semana=1).order_by('hr_grade')
                context['qua'] = Grade.objects.filter(dt_semana=2).order_by('hr_grade')
                context['qui'] = Grade.objects.filter(dt_semana=3).order_by('hr_grade')
                context['sex'] = Grade.objects.filter(dt_semana=4).order_by('hr_grade')
                context['sab'] = Grade.objects.filter(dt_semana=5).order_by('hr_grade')
                context['dom'] = Grade.objects.filter(dt_semana=6).order_by('hr_grade')

            except:
                Http404
            return context
        else:
            raise Http404
