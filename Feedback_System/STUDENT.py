from django.shortcuts import render, redirect
from app.models import Student,Student_Feedback,Course,FeedbackForm


def HOME(request):
    return render(request, 'STUDENT/student_home.html')


def STUDENT_FEEDBACK(request):
    return render(request, 'STUDENT/feedback.html')


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':

        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)
        feedbacks = Student_Feedback(
            student_id=student,
            feedback=feedback,
        )
        feedbacks.save()
    return redirect('student_feedback')



def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access selected answers using form.cleaned_data
            # For example, form.cleaned_data['Question 1'] will give the selected answer for Question 1
            # You can save the feedback data to your database or perform other actions.
            pass
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
