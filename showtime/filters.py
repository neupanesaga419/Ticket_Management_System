from datetime import datetime
from django_filters import rest_framework as filter

from showtime.models import ShowTime, Shows


class MyDateFilter(filter.FilterSet):
    year = filter.NumberFilter(field_name="show_start_time", lookup_expr="year")
    month = filter.NumberFilter(field_name="show_start_time", lookup_expr="month")
    date = filter.NumberFilter(field_name="show_start_time", lookup_expr="day")
    hour = filter.NumberFilter(field_name="show_start_time", lookup_expr="hour")

    class Meta:
        model = ShowTime
        fields = ["show_start_time",]

    def __init__(self, data, *args, **kwargs):
        if not data.get('date'):
            data = data.copy()
            data['date'] = datetime.now().strftime("%d")
        super().__init__(data, *args, **kwargs)

    # def filter_day(self, queryset, key, value):
    #     id_list = queryset.values_list("id", flat=True)
    #     filtered_shows = Shows.objects.filter(show_time__id__in=id_list)
    #     return filtered_shows

