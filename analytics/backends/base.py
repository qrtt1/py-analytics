

class BaseAnalyticsBackend(object):
    _analytics_backend = None

    def track_count(self, unique_identifier, metric, inc_amt=1, **kwargs):
        """
        Tracks a metric just by count. If you track a metric this way, you won't be able
        to query the metric by day, week or month.

        :param unique_identifier: Unique string indetifying the object this metric is for
        :param metric: A unique name for the metric you want to track
        :param inc_amt: The amount you want to increment the ``metric`` for the ``unique_identifier``
        :return: ``True`` if successful ``False`` otherwise
        """
        return self._analytics_backend.incr("analy:%s:count:%s" % (unique_identifier, metric), inc_amt)

    def track_metric(self, unique_identifier, metric, date, inc_amt=1, **kwargs):
        """
        Tracks a metric for a specific ``unique_identifier`` for a certain date.

        TODO: Possibly default date to the current date.

        :param unique_identifier: Unique string indetifying the object this metric is for
        :param metric: A unique name for the metric you want to track
        :param date: A python date object indicating when this event occured
        :param inc_amt: The amount you want to increment the ``metric`` for the ``unique_identifier``
        :return: ``True`` if successful ``False`` otherwise
        """
        raise NotImplementedError()

    def get_metric_by_day(self, unique_identifier, metric, from_date, num_of_days=10):
        """
        Returns the ``metric`` for ``unique_identifier`` segmented by day
        starting from``from_date``

        :param unique_identifier: Unique string indetifying the object this metric is for
        :param metric: A unique name for the metric you want to track
        :param from_date: A python date object
        :param num_of_days: The total number of days to retrive starting from ``from_date``
        """
        raise NotImplementedError()

    def get_metric_by_week(self, unique_identifier, metric, from_date, num_of_weeks=10):
        """
        Returns the ``metric`` for ``unique_identifier`` segmented by week
        starting from``from_date``

        :param unique_identifier: Unique string indetifying the object this metric is for
        :param metric: A unique name for the metric you want to track
        :param from_date: A python date object
        :param num_of_weeks: The total number of weeks to retrive starting from ``from_date``
        """
        raise NotImplementedError()

    def get_metric_by_month(self, unique_identifier, metric, from_date, num_of_months=10):
        """
        Returns the ``metric`` for ``unique_identifier`` segmented by month
        starting from``from_date``. It will retrieve metrics data starting from the 1st of the
        month specified in ``from_date``

        :param unique_identifier: Unique string indetifying the object this metric is for
        :param metric: A unique name for the metric you want to track
        :param from_date: A python date object
        :param num_of_months: The total number of months to retrive starting from ``from_date``
        """
        raise NotImplementedError()

    def get_backend(self):
        return self._analytics_backend
