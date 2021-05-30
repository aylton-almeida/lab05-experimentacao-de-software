import json

import requests
from requests.models import Response

from src.models.GithubException import GithubException


class Graphql:

    url: str
    repos_per_request: int
    cursor = None
    createdAt: str

    def __init__(self, url: str, repos_per_request: int) -> None:
        self.url = url
        self.repos_per_request = repos_per_request

    def get_repo_query(self, name: str, owner: str):
        return """
               query getIssues {
                 repository(name: "%(name)s", owner: "%(owner)s") {
                   issues(first: 100, after: %(after)s) {
                   edges {
                     cursor
                     node {
                       closed
                       participants {
                         totalCount
                       }
                     }
                   }
                   }
                   }
                 }
               """ % {
            'repos': self.repos_per_request,
            'name': name,
            'owner': owner,
            'after': ('"{}"'.format(self.cursor) if self.cursor else 'null'),
        }

    def _fetch_data(self, query: str, token: str) -> dict:
        response: Response = requests.post(self.url, json={'query': query}, headers={
            'Authorization': token
        })

        if response.status_code != 200:
            raise GithubException(
                'There was an error while trying to make the request'
            )

        return json.loads(response.text)

    def get_issues_data(self, query: str, token: str):

        json_data = self._fetch_data(query, token)

    def get_repos_data(self, query: str, token: str):
        response: Response = requests.post(self.url, json={'query': query}, headers={
            'Authorization': token
        })

        if response.status_code != 200 or 'errors' in response.text:
            print(response.text)
            raise GithubException(
                'There was an error while trying to make the request'
            )

        json_data: dict = json.loads(response.text)

        edges: list = json_data['data']['repository']['issues']['edges']

        edges = [{**edge}
                 for edge in edges]

        return edges
