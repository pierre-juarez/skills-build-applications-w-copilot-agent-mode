from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Crear usuarios
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True)

        # Crear actividades
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-11-10')
        Activity.objects.create(user='Batman', type='cycle', duration=45, date='2025-11-09')
        Activity.objects.create(user='Wonder Woman', type='swim', duration=60, date='2025-11-08')
        Activity.objects.create(user='Spider-Man', type='climb', duration=25, date='2025-11-07')

        # Crear leaderboard
        Leaderboard.objects.create(team='marvel', points=120)
        Leaderboard.objects.create(team='dc', points=110)

        # Crear workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
