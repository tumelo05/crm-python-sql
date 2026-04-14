# python/run_crud_contacts.py
from crud_contacts import (
    get_contacts_by_company,
    update_contact
)

print("Contacts for Adams LLC:")
for c in get_contacts_by_company("Adams LLC"):
    print(c)

update_contact(
    email="amandadixon@testemail.com",
    title="Senior Geologist"
)

print("\nAfter update:")
for c in get_contacts_by_company("Adams LLC"):
    print(c)