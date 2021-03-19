import requests
import json
from random import randint


class PetStore:
    def add_pet(self):
        id = randint(1000, 9999)
        url = 'https://petstore.swagger.io/v2/pet'
        data = {"id": id, "name": "Naq"}
        headers = {'Content-type': 'application/json'}
        res = requests.post(url, json=data, headers=headers)
        pet_id = res.json()['id']
        assert res.status_code == 200, f'response status is {res.status_code} '
        assert id == pet_id, f'id validation error:pet_id = {pet_id}, generated id = {id}'
        return pet_id


    def check_pet(self, id):
        url = f'https://petstore.swagger.io/v2/pet/{id}'
        res = requests.get(url)
        pet_id = res.json()['id']
        pet_name = res.json()['name']
        assert res.status_code == 200, f'response status is {res.status_code} '
        assert id == pet_id, f'id validation error:pet_id = {pet_id}, generated id = {id}'
        return pet_id, pet_name


    def update_name(self, id, name):
        print(id, name)
        url = f'https://petstore.swagger.io/v2/pet'
        data = {"id": id, "name": name}
        headers = {'Content-type': 'application/json'}
        res = requests.put(url, json=data, headers=headers)
        pet_name = res.json()['name']
        assert res.status_code == 200, f'response status is {res.status_code}'
        assert name == pet_name, f'names are not equal: name:{name}, pet_name: {pet_name}'

    def check_pet_name(self, id, name):
        url = f'https://petstore.swagger.io/v2/pet/{id}'
        res = requests.get(url)
        pet_id = res.json()['id']
        pet_name = res.json()['name']
        assert res.status_code == 200, f'response status is {res.status_code} '
        assert id == pet_id, f'id validation error:pet_id = {pet_id}, generated id = {id}'
        assert name == pet_name,  f'names validation error:pet_name = {pet_name}, new name = {name}'

