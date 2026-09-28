# from django.shortcuts import render, redirect
# from .forms import FeedbackForm
# from .models import Feedback


# def feedback_list(request):
#     feedbacks = Feedback.objects.all()
#     return render(request, 'feedback_form/feedback_list.html', {
#         'feedbacks': feedbacks
#     })


# def feedback_create(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('feedback_list')
#     else:
#         form = FeedbackForm()

#     return render(request, 'feedback_form/feedback_form.html', {
#         'form': form
#     })from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback_form/feedback_list.html', {
        'feedbacks': feedbacks
    })


def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form/feedback_form.html', {
        'form': form
    })