from django.http import HttpResponse
from google.cloud import bigquery

from common.util import helper

# import os
import json

def index(request):
    return HttpResponse("Hello, world.")


def hacker_news(request):
    # Set up authentication
    helper.setup_google_adc()

    # Construct a BigQuery client object.
    client = bigquery.Client()

    query = """
        SELECT title, author, time_ts
        FROM `bigquery-public-data.hacker_news.stories`
        ORDER BY time_ts DESC
        LIMIT 5
    """

    query_job = client.query(query)

    records = [
        {
            'id': index,
            'title': row['title'],
            'author': row['author'],
            'dateOfPublication': str(row['time_ts'])
        } for index, row in enumerate(query_job)
    ]

    # Serialize obj to pretty-printed JSON
    dump = json.dumps(records, indent=4)

    return HttpResponse(dump, content_type='application/json')


def github(request):
    # Set up authentication
    helper.setup_google_adc()    

    # Construct a BigQuery client object.
    client = bigquery.Client()

    query = """
        SELECT committer.name AS committer_name, count(commit) AS total_commits 
        FROM `bigquery-public-data.github_repos.sample_commits`
        WHERE EXTRACT(YEAR FROM committer.date) = 2016 
        GROUP BY committer_name
        ORDER BY total_commits DESC;
    """

    query_job = client.query(query)

    records = [
        {
            'id': index,
            'committer_name': row['committer_name'],
            'total_commits': row['total_commits']
        } for index, row in enumerate(query_job)
    ]

    # Serialize obj to pretty-printed JSON
    dump = json.dumps(records, indent=4)

    return HttpResponse(dump, content_type='application/json')
