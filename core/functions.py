from django.utils import timezone


def find_entries_in_date_range(model_class, start_field, stop_field, date):
    date_day = date.day
    date_month = date.month

    lookup_args = {
        f"{start_field}__day__lte": date_day,
        f"{start_field}__month__lte": date_month,
        f"{stop_field}__day__gte": date_day,
        f"{stop_field}__month__gte": date_month,
    }

    entries_in_range = model_class.objects.filter(**lookup_args)
    return entries_in_range
