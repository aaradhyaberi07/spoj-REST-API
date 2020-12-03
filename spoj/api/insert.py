import os,csv,json,django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spoj.settings")
django.setup()

from .models import Problem

def inserter():
    with open('spoj.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                temp = json.dumps(row['tags'])
                p,created = Problem.objects.get_or_create(
                    name=row['name'], 
                    prob_id=row['id'],
                    url = row['link'],
                    tags = temp)
                if created:
                    p.save()
