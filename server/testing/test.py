import requests

# Define the base URLs for your Flask applications
BAKERY_BASE_URL = 'http://localhost:5555'  # Update the port if needed
GAME_BASE_URL = 'http://localhost:5556'    # Update the port if needed

# Test the Bakery and Baked Goods Application
def test_bakery_and_baked_goods():
    # Test fetching bakeries
    response = requests.get(f'{BAKERY_BASE_URL}/bakeries')
    print("Bakeries:")
    print(response.json())
    
    # Test fetching baked goods
    response = requests.get(f'{BAKERY_BASE_URL}/baked_goods')
    print("\nBaked Goods:")
    print(response.json())

# Test the Game Application
def test_game():
    # Test fetching games
    response = requests.get(f'{GAME_BASE_URL}/games')
    print("Games:")
    print(response.json())

# Main function to run tests
if __name__ == '__main__':
    print("Testing Bakery and Baked Goods Application...")
    test_bakery_and_baked_goods()
    
    print("\nTesting Game Application...")
    test_game()
