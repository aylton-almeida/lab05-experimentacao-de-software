import os

from dotenv import load_dotenv

from Graphql import Graphql

load_dotenv()

# Get env variables
graphql_url = os.getenv('GRAPHQL_URL')
rest_url = os.getenv('REST_URL')
token = os.getenv('AUTH_TOKEN')
