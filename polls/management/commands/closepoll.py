from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'       # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.pub_date = datetime.now() - timedelta(days=10)
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
