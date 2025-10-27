from src.api_client import get_all_countries

def test_country_count():
    response = get_all_countries()
    total_countries = len(response)
    assert total_countries == 195, f"Expected 195 countries, got {total_countries}"
