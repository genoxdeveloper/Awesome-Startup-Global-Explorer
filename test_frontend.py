import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_app():
    print("1. Fetching index page (English)...")
    r_en = requests.get(f"{BASE_URL}/")
    assert "Admin" in r_en.text, "Admin button missing"
    assert "langSel" in r_en.text, "Language selector missing"
    print("   ✅ English index loaded successfully.")
    
    print("2. Fetching API data (English)...")
    api_en = requests.get(f"{BASE_URL}/api/data?lang=en").json()
    assert 'records' in api_en, "API data missing records"
    first_record = api_en['records'][0]
    print(f"   ✅ First record: {first_record['title']}")
    assert 'deadline' in first_record, "Deadline missing"
    assert 'url' in first_record, "URL missing"
    assert first_record['title'] == first_record.get('translated_title', first_record['title']), "EN should not be translated differently"

    print("3. Fetching API data (Korean)...")
    api_ko = requests.get(f"{BASE_URL}/api/data?lang=ko").json()
    first_record_ko = api_ko['records'][0]
    print(f"   ✅ First record (KO): {first_record_ko['translated_title']} (Original: {first_record_ko['title']})")
    assert first_record_ko['translated_title'] != first_record_ko['title'], "Title was not translated to Korean!"

    print("4. Testing Admin API without key...")
    r_admin_fail = requests.post(f"{BASE_URL}/api/refresh")
    assert r_admin_fail.status_code == 401, "Admin API should fail without key"
    print("   ✅ Admin API blocked correctly.")
    
    print("5. Testing Admin API with key...")
    # Read the key from the environment or default
    r_admin_success = requests.post(f"{BASE_URL}/api/refresh", headers={"X-Admin-Key": "default-insecure-admin-key-change-me"})
    assert r_admin_success.status_code == 200, "Admin API should succeed with key"
    print("   ✅ Admin API succeeded with correct key.")
    
    print("\n🎉 ALL BROWSER-LEVEL TESTS PASSED!")

if __name__ == "__main__":
    test_app()
