from crud_accounts import get_all_accounts, get_account_by_name, update_account

print("First 3 accounts:")
for acc in get_all_accounts()[:3]:
    print(acc)

print("\nUpdating Adams LLC...")
update_account("Adams LLC", industry="Energy & Utilities")

print("\nUpdated account:")
print(get_account_by_name("Adams LLC"))