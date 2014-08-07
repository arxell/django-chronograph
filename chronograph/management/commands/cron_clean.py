from ...models import Log
from django.core.management.base import BaseCommand
from django.utils.timezone import now as tz_now
import datetime


class Command(BaseCommand):
    help = 'Deletes old job logs.'

    def handle( self, *args, **options ):
        if len(args) != 2:
            print 'Command requires two argument. Unit (weeks, days, hours or minutes) and interval.'
            return
        else:
            unit = str(args[ 0 ])
            if unit not in [ 'weeks', 'days', 'hours', 'minutes' ]:
                print 'Valid units are weeks, days, hours or minutes.'
                return
            try:
                amount = int( args[ 1 ] )
            except ValueError:
                print 'Interval must be an integer.'
                return
        kwargs = { unit: amount }
        time_ago = tz_now() - datetime.timedelta(**kwargs)
        Log.objects.filter( run_date__lte = time_ago ).delete()
