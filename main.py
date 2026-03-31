# src/main.py
from src.application.services.item_service import ItemService
from src.infrastructure.repositories.in_memory_item_repository import InMemoryItemRepository

def main():
    """Main function to demonstrate usage."""
    # Setup
    item_repository = InMemoryItemRepository()
    item_service = ItemService(item_repository)

    # Create items
    print("Creating items...")
    item1 = item_service.create_item(name="Laptop", description="A powerful laptop", price=1200.50)
    item2 = item_service.create_item(name="Mouse", description="A wireless mouse", price=25.00)
    print(f"Created item: {item1}")
    print(f"Created item: {item2}")
    print("-" * 20)

    # Get all items
    print("Getting all items...")
    all_items = item_service.get_all_items()
    for item in all_items:
        print(f"Found item: {item}")
    print("-" * 20)

    # Get a single item
    print(f"Getting item with ID: {item1.id}")
    retrieved_item = item_service.get_item(item1.id)
    print(f"Retrieved item: {retrieved_item}")
    print("-" * 20)

    # Update an item
    print(f"Updating price for item: {item1.id}")
    updated_item = item_service.update_item_price(item1.id, 1150.00)
    print(f"Updated item: {updated_item}")
    print("-" * 20)

    # Delete an item
    print(f"Deleting item with ID: {item2.id}")
    item_service.delete_item(item2.id)
    print("Item deleted.")
    print("-" * 20)

    # Verify deletion
    print("Getting all items after deletion...")
    all_items_after_delete = item_service.get_all_items()
    for item in all_items_after_delete:
        print(f"Found item: {item}")
    print("-" * 20)

if __name__ == "__main__":
    main()
