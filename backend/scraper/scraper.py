from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os


def scrape_data():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Set up the Chrome WebDriver
    chrome_driver_path = os.environ.get(
        'CHROMEDRIVER_PATH', '/usr/bin/chromedriver')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the page
    url = "https://highrollpoker.com/tracker/players"
    driver.get(url)

    # Wait for the table to load
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Give some time for JavaScript to fully render the content
    time.sleep(5)

    players = []
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip header row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 9:  # Ensure there are enough columns after skipping
            player = {
                "name": columns[3].text.strip(),
                "net_winnings": columns[4].text.strip(),
                "vpip": columns[5].text.strip(),
                "pfr": columns[6].text.strip(),
                "hours_played": columns[7].text.strip(),
                "hourly": columns[8].text.strip(),
                "bb_per_hour": columns[9].text.strip()
            }
            players.append(player)

    driver.quit()

    # Save the data to a JSON file
    with open('highroll_poker_data.json', 'w') as f:
        json.dump(players, f, indent=2)

    print(f"Scraped {len(players)} players")


if __name__ == "__main__":
    scrape_data()
