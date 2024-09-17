# players/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from players.models import Players, PlayerList
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating the database...')

        # Define sample data
        players_data = [
            {'username': 'Abdisalam', 'phone_number': '07306243707'},
            {'username': 'Ahmed', 'phone_number': '07346039707'},
            {'username': 'Mahad', 'phone_number': '07306054707'},
            {'username': 'Mascuud', 'phone_number': '07306039707'},
            {'username': 'Omar', 'phone_number': '07236039707'},
            {'username': 'Khalid', 'phone_number': '07306035607'},
            {'username': 'Issa', 'phone_number': '07306039712'},

        ]

        # Create Player objects
        for player_data in players_data:
            Players.objects.get_or_create(**player_data)

        # Create a PlayerList for the current game week
        current_week = datetime.now().isocalendar()[1]
        player_list, created = PlayerList.objects.get_or_create(game_week=current_week)

        # Optionally, add players to the PlayerList
        players = Players.objects.all()
        player_list.players.set(players)

        self.stdout.write('Database populated successfully.')
