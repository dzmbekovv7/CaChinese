from datetime import timedelta
from django.utils.timezone import now

def update_user_streak(user):
    profile = user.profile
    today = now().date()

    if profile.last_active:
        last_date = profile.last_active.date()

        if last_date == today:
            return

        elif last_date == today - timedelta(days=1):
            profile.streak += 1

        else:
            profile.streak = 1
    else:
        profile.streak = 1

    profile.last_active = now()
    profile.save()