from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from .models import Carousel, Content
from .forms import CarouselContentFormSet

class CarouselContentListView(ListView):
    model = Carousel

class CarouselContentCreateView(CreateView):
    model = Carousel
    success_url = reverse_lazy('carousel-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CarouselContentCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['carouselcontent'] = CarouselContentFormSet(self.request.POST, self.request.FILES)
        else:
            template_id = self.request.GET.get('template', None)
            # position = self.request.GET.get('position', None)
            context['carouselcontent'] = CarouselContentFormSet()
            if template_id:
                context['form'].initial['template'] = template_id
            # if position:
            #     context['form'].initial['position'] = position
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        carouselContent = context['carouselcontent']
        with transaction.atomic():
            if carouselContent.is_valid():
                self.object = form.save()
                carouselContent.instance = self.object
                carouselContent.save()
                return render(self.request, 'carrusel/carousel_create_success.html', {'carousel': self.object, 'type': "create"})
            else:
                return self.render_to_response(self.get_context_data(form=form))
        return super(CarouselContentCreateView, self).form_valid(form)

class CarouselContentUpdateView(UpdateView):
    model = Carousel
    success_url = reverse_lazy('carousel-list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CarouselContentUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['carouselcontent'] = CarouselContentFormSet(self.request.POST, self.request.FILES, instance=self.object)
            context['carouselcontent'].full_clean()
        else:
            template_id = self.request.GET.get('template', None)
            # position = self.request.GET.get('position', None)
            context['carouselcontent'] = CarouselContentFormSet(instance=self.object)
            if template_id:
                context['form'].initial['template'] = template_id
            # if position:
            #     context['form'].initial['position'] = position
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        carouselContent = context['carouselcontent']
        with transaction.atomic():
            if carouselContent.is_valid():
                self.object = form.save()
                carouselContent.instance = self.object
                carouselContent.save()
                return render(self.request, 'carrusel/carousel_create_success.html', {'carousel': self.object, 'type': "update"})
            else:
                return self.render_to_response(self.get_context_data(form=form))
        return super(CarouselContentUpdateView, self).form_valid(form)
