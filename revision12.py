from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize window
options.add_experimental_option("detach", True)  # Keeps Chrome open after script ends

driver = webdriver.Chrome(options=options)

# Open Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Wait for the page to load
time.sleep(3)

# Enter login credentials
username = driver.find_element(By.ID, "usernameField")
password = driver.find_element(By.ID, "passwordField")
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')

# Replace with your actual credentials
username.send_keys("onkarpatil272@gmail.com")
password.send_keys("Onkar@272")
login_button.click()

print("✅ Logged in successfully!")
time.sleep(5)

# Search for jobs
driver.get("https://www.naukri.com/aws-devops-jobs")
time.sleep(5)

# Get job links
job_links = driver.find_elements(By.XPATH, '//*[@id="listContainer"]//a[contains(@class, "title")]')

if not job_links:
    print("⚠️ No jobs found!")
    driver.quit()
    exit()

print(f"🔍 Found {len(job_links)} jobs.")

# Open each job in a new tab and apply
for job in job_links:
    job_url = job.get_attribute("href")
    driver.execute_script(f'window.open("{job_url}", "_blank");')
    time.sleep(3)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)

    try:
        # Check for the standard "Apply" button
        apply_button = driver.find_element(By.XPATH, '//button[contains(text(), "Apply")]')
        apply_button.click()
        print("✅ Applied for:", driver.title)

        # Close the tab and switch back
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except:
        try:
            # Check for "Apply on Company Site" button
            company_apply_button = driver.find_element(By.XPATH, '//a[contains(text(), "Apply on company site")]')
            print("🔗 Apply on Company Site found! Keeping tab open:", driver.title)
            # Don't close this tab; just switch back to the main tab
            driver.switch_to.window(driver.window_handles[0])

        except:
            print("❌ No Apply button found!")
            driver.close()  # Close tab if neither button is found
            driver.switch_to.window(driver.window_handles[0])

# Done
print("🎉 Finished applying to jobs.")

# Remove driver.quit() to keep Chrome open
# driver.quit()  # <-- REMOVE or COMMENT THIS LINE
