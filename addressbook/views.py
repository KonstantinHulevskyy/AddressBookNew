from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from .forms import CreatePersonForm
from .models import Person


class HomePageView(TemplateView):
    template_name = "addressbook/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = 'All Persons'
        if search_by in ['surname', 'name'] and search_by:
            if search_by == 'name':
                persons = Person.objects.filter(name=query)
                search_message = f'Searching for "name" by "{query}"'
            else:
                persons = Person.objects.filter(surname=query)
                search_message = f'Searching for "surname" by "{query}"'
        else:
            persons = Person.objects.all()
        context["Persons"] = persons
        context["search_message"] = search_message
        return context


class AddPersonFormView(CreateView):
    template_name = "addressbook/add_persone.html"
    form_class = CreatePersonForm
    success_url = reverse_lazy('home')


class DeletePersonView(DeleteView):
    model = Person
    template_name = "addressbook/delete_persone.html"
    success_url = reverse_lazy('home')


class EditPersonView(UpdateView):
    model = Person
    fields = [
        "name", "surname", "address",
        "phone_number", "url", "image"
    ]
    template_name = "addressbook/edit.html"
    success_url = reverse_lazy('home')
