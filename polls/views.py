import math

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .forms import ContactForm, TriangleForm  # , PersonForm
from .models import Choice, Person, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email="noreply@mysite.com",
                recipient_list=[form.cleaned_data['email']]
            )
            return redirect("polls:contact_form")
    else:
        form = ContactForm(initial={'email': 'test@test.com'})
    return render(request, 'contact_form.html', {
        'form': form,
    })


def triangle_form(request):
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            hypotenuse = math.sqrt(form.cleaned_data['a'] ** 2 + form.cleaned_data['b'] ** 2)
            hypotenuse = hypotenuse if hypotenuse % 1 != 0 else int(hypotenuse)  # Резало глаз
            return render(request, 'triangle_form.html', {
                'hypotenuse': hypotenuse,
            })
    else:
        form = TriangleForm()
    return render(request, 'triangle_form.html', {
        'form': form,
    })


class PersonListView(generic.ListView):
    model = Person
    paginate_by = 10


class PersonDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Person

    def author_detail_view(self, pk):
        # try:
        #     book_id=Book.objects.get(pk=pk)
        # except Book.DoesNotExist:
        #     raise Http404("Book does not exist")

        person_id = get_object_or_404(Person, pk=pk)
        return render(
            self,
            'polls/person_detail.html',
            context={'person': person_id, }
        )


class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('polls:persons')


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'email']
    instance = ['first_name', 'last_name']
    success_url = reverse_lazy('polls:persons')

    # В предыдущих методах вызывать get_or_404 явно не нужно так как там всё это
    # продумано более компетентными людьми под капотом в файле:строке
    # venv/lib/python3.10/site-packages/django/views/generic/detail.py:54


# def add_person(request):  # Специально для instance
#     if request.method == "POST":
#         form = PersonForm(request.POST, instance=Person())
#         if form.is_valid():
#             person = form.save()        # noqa: F841
#             return redirect("polls:persons")
#     else:
#         form = PersonForm(instance=Person())
#
#     return render(request, 'polls/person_form.html', {
#         'form': form,
#     })
