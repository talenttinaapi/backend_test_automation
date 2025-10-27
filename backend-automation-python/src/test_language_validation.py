from src.api_client import get_all_countries

def test_language_validation():
    response = get_all_countries()
    south_africa = next((country for country in response if country["cca2"] == "ZA"), None)
    assert south_africa is not None, "South Africa not found in API response."
    languages = south_africa.get("languages", {})
    assert any("sign" in lang.lower() or "sas" in lang.lower() for lang in languages.values()),         f"Expected SASL in South Africa's languages, found: {languages}"
