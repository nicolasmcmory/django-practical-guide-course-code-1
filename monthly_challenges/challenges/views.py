from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .services import Month_challenges
from django.template.loader import render_to_string


# Views
def challenges_by_month_str(request, month: str):
    # Init month challenges
    month_challenges = Month_challenges()

    try:
        challenge = month_challenges.get_challenge_str(month)
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    
    except Exception as e:
        return HttpResponseNotFound(f"Month doesn't exist. Cause: {e}")



def challenges_by_month_int(request, month: int):
    # Init month challenges
    month_challenges = Month_challenges()
    month = month_challenges.get_month_from_num(month)

    # Test if month is Exception
    if isinstance(month, Exception):
        return HttpResponseNotFound(month)

    else:
        redirect_str = reverse("challenges_by_month", args=[month])
        return HttpResponseRedirect(redirect_str)


def challenges(request):
    # Init month challenges
    months = Month_challenges().get_list_months()

    response_content = "<ul>"

    for month in months:
        month_link = reverse("challenges_by_month", args=[month])
        response_content += (
            f'<li><a href = "{month_link}">{month.capitalize()}</a></li>'
        )

    response_content += "</ul>"

    return HttpResponse(response_content)
