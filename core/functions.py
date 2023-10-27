from django.utils import timezone
from datetime import date
from django.db.models import Func, F, Value


# filter all entries in model_class, where the week (0-52) of the selected current_date falls between the week of start and stop date (date objects)
def find_entries_in_date_range(model_class, start_field, stop_field, current_date):
    current_week = current_date.isocalendar()[1]

    lookup_args = {
        f"{start_field}__week__lte": current_week,
        f"{stop_field}__week__gte": current_week,
    }
    entries_in_range = model_class.objects.filter(**lookup_args)
    return entries_in_range
