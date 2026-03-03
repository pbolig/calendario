import json
from django.core.management.base import BaseCommand
from core.models import Category, Event
from datetime import datetime

class Command(BaseCommand):
    help = 'Importar datos desde planificacion_iset.json'

    def handle(self, *args, **options):
        with open('planificacion_iset.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Importar Categorías
        for cat_data in data.get('categories', []):
            Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'color': cat_data['color']}
            )
        self.stdout.write(self.style.SUCCESS('Categorías importadas.'))

        # Importar Eventos
        events_data = data.get('events', {})
        for date_str, ev_list in events_data.items():
            # El formato en el JSON parece ser YYYY-M-D (ej: 2026-2-9)
            # Django requiere YYYY-MM-DD o un objeto date
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                # Reintentar con otro posible formato o saltar
                self.stdout.write(self.style.WARNING(f'Formato de fecha inválido: {date_str}'))
                continue

            for ev in ev_list:
                cat_name = ev.get('cat')
                desc = ev.get('desc', '')
                
                category = Category.objects.filter(name=cat_name).first()
                if category:
                    Event.objects.create(
                        date=date_obj,
                        category=category,
                        description=desc
                    )
        
        self.stdout.write(self.style.SUCCESS('Eventos importados exitosamente.'))
