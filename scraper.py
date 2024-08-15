from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up the Chrome WebDriver
service = Service('/usr/bin/chromedriver')  # Update this path if necessary
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
            # Skip the first three columns, use index 3 for name
            "name": columns[3].text.strip(),
            "net_winnings": columns[4].text.strip(),  # Net winnings
            "vpip": columns[5].text.strip(),  # VPIP
            "pfr": columns[6].text.strip(),  # PFR
            "hours_played": columns[7].text.strip(),  # Hours Played
            "hourly": columns[8].text.strip(),  # Hourly $
            "bb_per_hour": columns[9].text.strip()  # BB/Hour
        }
        players.append(player)

driver.quit()

# Save the data to a JSON file
with open('highroll_poker_data.json', 'w') as f:
    json.dump(players, f, indent=2)

print(f"Scraped {len(players)} players")
print("First player data:")
print(json.dumps(players[0], indent=2))

