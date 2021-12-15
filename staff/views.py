from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView, View, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from visitors.models import CommonQuestion, Review
from visitors.forms import CommonQuestionForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


class CommonQuestionCreateView(CreateView, UserPassesTestMixin):
    template_name = 'common_question_form.html'
    success_url = reverse_lazy('common_questions')
    model = CommonQuestion
    form_class = CommonQuestionForm

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class CommonQuestionDeleteView(DeleteView, UserPassesTestMixin):
    model = CommonQuestion
    template_name = 'delete_view.html'
    success_url = reverse_lazy('common_questions')
    success_message = "The question was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(CommonQuestionDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff


class CommonQuestionUpdateView(UpdateView, UserPassesTestMixin):
    template_name = 'common_question_form.html'
    model = CommonQuestion
    form_class = CommonQuestionForm
    success_url = reverse_lazy('common_questions')

    def form_valid(self, form):
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_staff


@staff_member_required
def evaluate_review(request, review_id, published):
    review = Review.objects.get(id=review_id)
    if published:
        review.visible = True
        review.save()
        return redirect('reviews')
    else:
        review.visible = False
        review.save()
        return redirect('delete_review', review_id)


class ReviewDeleteView(DeleteView, UserPassesTestMixin):
    model = Review
    template_name = 'delete_view.html'
    success_url = reverse_lazy('reviews')
    success_message = "The review was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message  % obj.__dict__)
        return super(ReviewDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_staff
