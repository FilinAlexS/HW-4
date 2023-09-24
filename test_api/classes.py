import requests


class Dogceo:
    @staticmethod
    def get_list_breads():
        list_breeds_dogs = requests.get('https://dog.ceo/api/breeds/list/all')
        return list_breeds_dogs.json()['message'].keys()


class Brewery:
    @staticmethod
    def get_brewery_id(item=0):
        list_brewery = requests.get('https://api.openbrewerydb.org/v1/breweries?per_page=10')
        return list_brewery.json()[item]['id']
