import riak

dbConnection = riak.RiakClient(pb_port=8087)
bucket = dbConnection.bucket("S8901")

input = {"name": "Donnie", "surname": "Boettcher", "age": 35, "height": 180, "isMarried": True}

file = open('komunikaty.txt','w')

print >>file, 'Wrzucenie, pobranie, wypisanie:'
keyToStore = bucket.new(input["surname"], data=input)
keyToStore.store()
storedKey = bucket.get(input["surname"])
print >>file, storedKey.encoded_data + "\n"

print >>file, 'Modyfikacja, pobranie, wypisanie:'
storedKey.data["age"] = 36
storedKey.store()
editedKey = bucket.get(input["surname"])
print >>file, editedKey.encoded_data + "\n"

print >>file, 'Usuniecie, pobranie:'
editedKey.delete()
deletedKey = bucket.get(input["surname"])
print >>file, str(deletedKey.encoded_data) + "\n"

