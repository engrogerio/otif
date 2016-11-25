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
            context['week_days'] = range(0,7)
            context['hours'] = range(0,24)
            cliente='ABCD'
            context['cliente'] = cliente
            context['hora'] = Grade.objects.all()
            hr=[]
            try:
                for semana in range(0,7):
                    for hora in range(0,24):
                        hr.append(Grade.objects.filter(hr_grade=hora).filter(dt_semana=semana))

            except:
                Http404
            context['hr']=hr
            return context
        else:
            raise Http404

class GradeDetailView(generic.DetailView):
    template_name = 'grade_detail.html'
    model = Grade

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated():
            context = super(GradeDetailView, self).get_context_data(**kwargs)
            context['grade'] = Grade.objects.get(id=85)
            return context
        else:
            raise Http404

    def grade_detail(self,request, id=None):
        if request.user.is_authenticated():
            context={'a':1}
            return render(request, "treinamento_detail.html", context)
        else:
            raise Http404