from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View


# Using class-based views
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    # Handle POST request when the form is submitted and update the existing review if the user has already submitted one, otherwise create a new review.
    def post(self, request):
        submitted_data = request.POST
        try:
            user_name = submitted_data.get("user_name")
            db_instance = Review.objects.filter(user_name=user_name).first()

        except Review.DoesNotExist:
            print("No review found for this user, creating a new one.")
            db_instance = None

        form = ReviewForm(request.POST, instance=db_instance)

        if form.is_valid():
            # Using forms when using ModelForm is more efficient than manually creating an instance of the model and saving it, as it handles validation and data processing for you. I only works for simple forms, if you have more complex logic, you might want to manually create an instance of the model and save it.
            form.save()
            # review = Review(
            #         user_name=form.cleaned_data["user_name"],
            #         review_text=form.cleaned_data["review_text"],
            #         rating=form.cleaned_data["rating"],
            #     )
            #     review.save()
            return HttpResponseRedirect("/thank-you")

        else:
            return self.get(request)


# Using function-based views
""" def review(request):

    if request.method == "POST":
        existing_reviews = Review.objects.get(pk=1)
        form = ReviewForm(request.POST, instance=existing_reviews)

        if form.is_valid():
            form.save()
            # review = Review(
            #     user_name=form.cleaned_data["user_name"],
            #     review_text=form.cleaned_data["review_text"],
            #     rating=form.cleaned_data["rating"],
            # )
            # review.save()
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form}) """


def thank_you(request):
    return render(request, "reviews/thank_you.html")
