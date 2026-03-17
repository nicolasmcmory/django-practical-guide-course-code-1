from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView


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
            form.save()trl + p binding for 
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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Your information has been successfully susmitted."
        return context


class ReviewsView(View):
    def get(self, request):
        reviews = Review.objects.all()
        favorite = request.session.get("favorite_review")
        # Add an is_favorite attribute to each review object to indicate whether it is the user's favorite review or not, and pass this information to the template. This is dynamic and doesn't require any changes to the database schema, and it allows you to easily display the favorite review in the template without having to query the database again.
        for review in reviews:
            review.is_favorite = review.id == favorite
        return render(request, "reviews/reviews.html", {"reviews": reviews})


class ReviewDetail(View):
    def get(self, request, review_id):
        review = Review.objects.get(pk=review_id)
        return render(
            request,
            "reviews/review_detail.html",
            {
                "review": review,
                "favorite": review_id == request.session.get("favorite_review"),
            },
        )


class AddFavoriteView(View):
    def post(self, request):
        review_id = int(request.POST["review_id"])
        request.session["favorite_review"] = review_id
        redirect_url = reverse("review-detail", kwargs={"review_id": review_id})
        return HttpResponseRedirect(redirect_url)
