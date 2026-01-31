# %%
class Month_challenges:

    def __init__(self):
        self.month_challenges = {
            "january": "Eat no meat for the entire month!",
            "february": "Walk for at least 20 minutes every day!",
            "march": "Learn Django for at least 20 minutes every day!",
            "april": "Eat no meat for the entire month!",
            "may": "Walk for at least 20 minutes every day!",
            "june": "Learn Django for at least 20 minutes every day!",
            "july": "Eat no meat for the entire month!",
            "august": "Walk for at least 20 minutes every day!",
            "september": "Learn Django for at least 20 minutes every day!",
            "october": "Eat no meat for the entire month!",
            "november": "Walk for at least 20 minutes every day!",
            "december": None,
        }
        self.list_of_months = list(self.month_challenges.keys())

    def get_challenge_str(self, month: str) -> str:
        return self.month_challenges[month]

    def get_month_from_num(self, month: int) -> str | bool:
        # Type recasting
        month = int(month)

        # Test if is int and in range
        if isinstance(month, int) and month > 0 and month < 13:
            return self.list_of_months[month - 1]
        else:
            return Exception("Month number out of range.")
    
    def get_list_months(self):
        return self.list_of_months
