from playwright.sync_api import sync_playwright

def verify_dom():
    with sync_playwright() as p:
        print("Launching headless browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to http://127.0.0.1:5000...")
        response = page.goto("http://127.0.0.1:5000")
        
        if not response.ok:
            print(f"Failed to load page. Status: {response.status}")
            return
            
        print("Page loaded successfully.")
        
        # Wait for the table body to populate
        page.wait_for_selector("#tableBody tr", timeout=10000)
        
        # Check if the deadline filter exists
        deadline_filter = page.locator("#deadlineSel")
        if deadline_filter.count() > 0:
            print("✅ Deadline filter (#deadlineSel) found in DOM.")
            options = deadline_filter.locator("option").all_inner_texts()
            print(f"   Options available: {options}")
        else:
            print("❌ Deadline filter (#deadlineSel) NOT found!")

        # Verify the top cards exist
        top_cards = page.locator(".top-card").count()
        print(f"✅ Found {top_cards} Top Cards in DOM.")
        
        # Verify table rows exist
        table_rows = page.locator("#tableBody tr").count()
        print(f"✅ Found {table_rows} Table Rows in DOM.")
        
        # Check for Apply buttons
        apply_buttons = page.locator(".btn-apply").count()
        print(f"✅ Found {apply_buttons} 'Apply' buttons in DOM.")
        
        # Check loading overlay style
        loading_overlay = page.locator("#loadingOverlay")
        if loading_overlay.count() > 0:
            print("✅ Loading overlay found.")
            # Verify if it's positioned absolute (inside table-container)
            is_absolute = page.evaluate("window.getComputedStyle(document.getElementById('loadingOverlay')).position === 'absolute'")
            if is_absolute:
                print("   ✅ Loading overlay is correctly styled as 'absolute' (not blocking entire screen).")
            else:
                print("   ❌ Loading overlay is NOT absolute! It might be blocking the screen.")
                
        # Take a screenshot
        page.screenshot(path="dom_verification.png", full_page=True)
        print("📸 Screenshot saved as dom_verification.png")
        
        browser.close()
        print("DOM Verification Complete.")

if __name__ == "__main__":
    verify_dom()
