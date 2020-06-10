from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cocktail, Evaluation
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, CocktailAddForm, AddRatingForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


def main(request: HttpRequest):
    context = {
        'title': 'Главная страница',
        'items': Cocktail.objects.all()
    }
    return render(request, "main.html", context)


def detailed_view(request: HttpRequest, pk: int):
    cocktail = get_object_or_404(Cocktail, id=pk)
    context = {
        'title': f'{cocktail.title}',
        'cocktail': cocktail
    }
    return render(request, "detailed_view.html", context)


@login_required
def add_rating(request: HttpRequest, pk: int):
    form = AddRatingForm()
    if request.method == 'POST':
        form = AddRatingForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(Cocktail, id=pk)
            form = form.save(commit=False)
            form.user = request.user
            form.cocktail = item
            form.save()
            items = list(Evaluation.objects.filter(cocktail=item).values('evaluation'))
            a = [e['evaluation'] for e in items]
            item.rating = int(sum(a)/len(a))
            item.save()
            return redirect(reverse("detailed_view", kwargs={'pk': item.id}))
    return render(request, "form.html", {'form': form})


@login_required
def remove_view(request: HttpRequest, pk: int):
    item = get_object_or_404(Cocktail, id=pk)
    if item.author == request.user:
        item.delete()
        return redirect(reverse('main'))
    return redirect(reverse("detailed_view", kwargs={'pk': item.id}))


class UserCreationView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse("login")

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Infos successfully create user"
        )
        return super().form_valid(form)


user_creation_view = UserCreationView.as_view()


class CocktailCreationView(LoginRequiredMixin, CreateView):
    model = Cocktail
    form_class = CocktailAddForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse("main")

    def form_valid(self, form):
        form.instance.author = self.request.user

        messages.add_message(
            self.request, messages.INFO, "Infos successfully create cocktail"
        )
        return super().form_valid(form)


cocktail_creation_view = CocktailCreationView.as_view()


class CocktailUpdateView(LoginRequiredMixin, UpdateView):
    model = Cocktail
    form_class = CocktailAddForm
    template_name = 'form.html'
    slug_field = 'id'

    def get_success_url(self):
        return reverse("detailed_view", kwargs={'pk': self.object.id})

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, "Infos successfully update cocktail"
        )
        return super().form_valid(form)


cocktail_update_view = CocktailUpdateView.as_view()


def search(request: HttpRequest):
    return render(request, 'search.html', context={'title': 'Поиск'})
