from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from catalog.forms import AuthorsForm
from catalog.models import Book, BookInstance, Authors


def authors_add(request):
    author = Authors.objects.all()
    authorsform = AuthorsForm()
    return render(request, 'catalog/authors_add.html', {'form': authorsform, 'author': author})


def create(request):
    if request.method == 'POST':
        author = Authors()
        author.firstName = request.POST.get('firstName')
        author.lastName = request.POST.get('lastName')
        author.dateOfBirth = request.POST.get('dateOfBirth')
        author.dateOfDeath = request.POST.get('dateOfDeath')
        author.save()
        return HttpResponseRedirect('/authors_add/')


def delete(request, id):
    try:
        author = Authors.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/authors_add/')
    except Authors.DoesNotExist:
        return HttpResponseNotFound('<h2>Автор не найден</h2>')


def edit1(request, id):
    author = Authors.objects.get(id=id)
    if request.method == 'POST':
        author.firstName = request.POST.get('firstName')
        author.lastName = request.POST.get('lastName')
        author.dateOfBirth = request.POST.get('dateOfBirth')
        author.dateOfDeath = request.POST.get('dateOfDeath')
        author.save()
        return HttpResponseRedirect('/authors_add/')
    return render(request, 'edit1.html', {'author': author})


def index(request):
    numBooks = Book.objects.all().count()
    numInstances = BookInstance.objects.all().count()
    numInstancesAvailable = BookInstance.objects.filter(status__exact=2).count()
    numAuthors = Authors.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={
        'numBooks': numBooks,
        'numInstances': numInstances,
        'numInstancesAvailable': numInstancesAvailable,
        'numAuthors': numAuthors,
        'num_visits': num_visits
    })


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorsListView(generic.ListView):
    model = Authors
    paginate_by = 2


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Универсальный класс представления списка книг,
    находящийся в заказе у текущего пользователя.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('dueBack')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
