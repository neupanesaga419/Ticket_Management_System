from datetime import date
from django_filters import rest_framework as filter

from showtime.models import ShowTime


class MyDateFilter(filter.FilterSet):

    filter_date = filter.DateTimeFilter(field_name="show_start_time", lookup_expr="date")

    class Meta:
        model = ShowTime
        fields = ["show_start_time",]

    def __init__(self, data, *args, **kwargs):
        if not data.get('filter_date'):
            data = data.copy()
            data['filter_date'] = date.today()
        super().__init__(data, *args, **kwargs)


