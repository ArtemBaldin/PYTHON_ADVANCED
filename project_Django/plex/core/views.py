from core.models import Teacher

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    model = Teacher

    def get_context_data(self, **kwargs):
        teachers = Teacher.objects.all()
        context = {}

        for key, value in self.request.GET.items():
            if value != "":
                teachers = teachers.filter(**{key: value})
                context.setdefault(key, value)

        context.setdefault('teachers', teachers)
        return context
