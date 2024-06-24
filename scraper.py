from selenium import webdriver # provides API to interact with browser
from selenium.webdriver.chrome.service import Service # manages execution of the Chrome Browser
from selenium.webdriver.chrome.options import Options # 
from webdriver_manager.chrome import ChromeDriverManager # ensure up to date chrome driver is installed 
from bs4 import BeautifulSoup # parsing HTML 
import time

# Set up Chrome WebDriver
chrome_options = Options() 
chrome_options.add_argument("--headless")  # Run Chrome without the GUI (headless mode)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the webpage
url = "Enter URL here"
driver.get(url)

# Wait for JavaScript to load (you might need to adjust the wait time)
time.sleep(5)  # Wait for 5 seconds for JavaScript to load

# Extract the page source after JavaScript rendering
page_source = driver.page_source

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract text content
text_content = soup.get_text()

# Print the extracted content
print(text_content)

# Close the WebDriver
driver.quit()

