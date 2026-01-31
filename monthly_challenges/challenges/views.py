from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from .services import Month_challenges
from django.template.loader import render_to_string


# Views
def challenges_by_month_str(request, month: str):
    # Init month challenges
    month_challenges = Month_challenges()

    try:
        challenge = month_challenges.get_challenge_str(month)
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge, "month": month},
        )

    except Exception as e:
        raise Http404(e)


def challenges_by_month_int(request, month: int):
    # Init month challenges
    month_challenges = Month_challenges()
    month = month_challenges.get_month_from_num(month)

    # Test if month is Exception
    if isinstance(month, Exception):
        raise Http404()

    else:
        redirect_str = reverse("challenges_by_month", args=[month])
        return HttpResponseRedirect(redirect_str)


def index(request):
    # Init month challenges
    months = Month_challenges().get_list_months()

    return render(request, "challenges/index.html", {"months": months})

    # response_content = "<ul>"

    # for month in months:
    #     month_link = reverse("challenges_by_month", args=[month])
    #     response_content += (
    #         f'<li><a href = "{month_link}">{month.capitalize()}</a></li>'
    #     )

    # response_content += "</ul>"

    # return HttpResponse(response_content)
