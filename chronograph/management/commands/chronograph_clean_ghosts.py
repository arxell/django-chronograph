import os
import socket

from ...models import Job
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Sets jobs as not running if there is no process with job pid.'

    def handle(self, *args, **options):
        running_jobs = Job.objects.filter(host=socket.gethostname(), is_running=True)
        for job in running_jobs:
            if not pid_exists(job.pid):
                print 'setting job with pid {} as not running (no pid found in os)'.format(job.pid)
                job.is_running = False
                job.pid = None
                job.host = None
                job.save(update_fields=['is_running', 'pid', 'host'])


def pid_exists(pid):
    """
        Check For the existence of a unix pid.
        Source: http://stackoverflow.com/a/568285/1245140
    """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
