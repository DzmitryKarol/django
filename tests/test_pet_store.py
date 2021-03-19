from pages.pet_store_api import PetStore


def test_add_pet():
    new_pet = PetStore()
    id = new_pet.add_pet()
    new_pet.check_pet(id)
    new_name = 'Tuzik'
    new_pet.update_name(id, new_name)
    new_pet.check_pet_name(id, new_name)





