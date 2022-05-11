from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/noxferatu/Documents/projects/takehomeassignment/chromedriver"
driver = webdriver.Chrome(PATH)

# Test 1 Correct default landing page.
print("\nTest: Correct default landing page.\n")
driver.get("https://rstudio.cloud/content/yours")

try:
    pageload = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "app"))
    )
except:
    print("Test Failed: Page did not load")
    driver.quit()

assert driver.title == "RStudio Cloud", "Page title is not RStudio Cloud"
pageheader = driver.find_element_by_id("headerTitle")
assert pageheader.text == "Your Workspace", "Did not land on Your Workspace"
print("\nTest complete: Landed on Correct Page.\n")

# Test 2: Creation of new project and IDE loads by default
print("\nTest: Creation of new project and IDE loads by default.\n")
driver.find_element_by_css_selector(".action.menuDropDown.withActionTitle.imageRight.alwaysShowTitle").click()
driver.find_element_by_css_selector(".action.newRStudioProject").click()



try:
    iframeload = WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "contentIFrame"))
    )
except:
    print("failed to find container")
    driver.quit()

try:
    consoleload = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rstudio_shell_widget"))
    )
except:
    print("console not found")
    driver.quit()


print("\nTest complete: New project created and IDE loaded.\n")

# Test 3: Run Demo in IDE
print("\nTest: Run Demo in IDE\n")

# consoleentry = driver.find_element_by_id("rstudio_console_input")
# consoleentry.send_keys("demo(error.catching)")
# consoleentry.send_keys(Keys.RETURN)
# consoleentry.send_keys(Keys.RETURN)

