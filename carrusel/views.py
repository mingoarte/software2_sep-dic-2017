from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Carousel, Content
from .forms import CarouselFormSet

# Carousel Views
class CarouselListView(ListView):
    model = Carousel

class CarouselCreateView(CreateView):
    model = Carousel
    success_url = reverse_lazy('carousel-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CarouselCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['carousel_formset'] = CarouselFormSet(self.request.POST)
        else:
            context['carousel_formset'] = CarouselFormSet()
        print("context: ", context)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['carousel_formset']
        print("formset: ", formset)
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CarouselUpdateView(UpdateView):
    model = Carousel
    success_url = reverse_lazy('carousel-list')

    def get_context_data(self, **kwargs):
        context = super(CarouselUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['carousel_formset'] = CarouselFormSet(self.request.POST, instance=self.object)
            context['carousel_formset'].full_clean()
        else:
            context['carousel_formset'] = CarouselFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['carousel_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
