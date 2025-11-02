"""
Automated Login Testing with Selenium
Demonstrates AI-enhanced test automation patterns
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class LoginTestAutomation:
    def __init__(self, url):
        """Initialize the test automation framework"""
        self.url = url
        self.driver = None
        self.test_results = []

    def setup(self):
        """Setup WebDriver"""
        self.driver = webdriver.Chrome()  # or webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(2)  # Wait for page load

    def teardown(self):
        """Cleanup after tests"""
        if self.driver:
            self.driver.quit()

    def test_valid_login(self, username, password):
        """
        Test Case 1: Valid Login Credentials
        AI Enhancement: Intelligent wait and dynamic element detection
        """
        test_name = "Valid Login Test"
        try:
            # Find and fill username field (AI helps identify multiple selector strategies)
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)

            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)

            # Click login button
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Wait for successful login indicator
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "dashboard"))
            )

            self.test_results.append({
                "test": test_name,
                "status": "PASS",
                "message": "Successfully logged in with valid credentials"
            })
            return True

        except TimeoutException:
            self.test_results.append({
                "test": test_name,
                "status": "FAIL",
                "message": "Login failed - dashboard not found"
            })
            return False
        except Exception as e:
            self.test_results.append({
                "test": test_name,
                "status": "ERROR",
                "message": f"Unexpected error: {str(e)}"
            })
            return False

    def test_invalid_login(self, username, password):
        """
        Test Case 2: Invalid Login Credentials
        AI Enhancement: Error message detection and validation
        """
        test_name = "Invalid Login Test"
        try:
            # Navigate back to login if needed
            self.driver.get(self.url)
            time.sleep(1)

            # Fill credentials
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)

            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)

            # Click login
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Check for error message
            error_message = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )

            if error_message.is_displayed():
                self.test_results.append({
                    "test": test_name,
                    "status": "PASS",
                    "message": f"Error message displayed correctly: {error_message.text}"
                })
                return True
            else:
                self.test_results.append({
                    "test": test_name,
                    "status": "FAIL",
                    "message": "Error message not displayed"
                })
                return False

        except TimeoutException:
            self.test_results.append({
                "test": test_name,
                "status": "FAIL",
                "message": "Error message not found within timeout"
            })
            return False
        except Exception as e:
            self.test_results.append({
                "test": test_name,
                "status": "ERROR",
                "message": f"Unexpected error: {str(e)}"
            })
            return False

    def test_empty_credentials(self):
        """
        Test Case 3: Empty Credentials
        AI Enhancement: Boundary condition testing
        """
        test_name = "Empty Credentials Test"
        try:
            self.driver.get(self.url)
            time.sleep(1)

            # Try to login without entering credentials
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login-button"))
            )
            login_button.click()

            # Check if validation message appears
            validation_msg = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "validation-error"))
            )

            self.test_results.append({
                "test": test_name,
                "status": "PASS",
                "message": "Validation error displayed for empty fields"
            })
            return True

        except:
            self.test_results.append({
                "test": test_name,
                "status": "FAIL",
                "message": "No validation for empty credentials"
            })
            return False

    def run_test_suite(self):
        """Execute all test cases and generate report"""
        print("=" * 60)
        print("AI-ENHANCED LOGIN TEST AUTOMATION")
        print("=" * 60)

        self.setup()

        # Test scenarios
        print("\nRunning Test Suite...")
        self.test_valid_login("testuser@example.com", "ValidPass123!")
        self.test_invalid_login("invalid@example.com", "WrongPassword")
        self.test_empty_credentials()

        self.teardown()

        # Generate report
        self.generate_report()

    def generate_report(self):
        """Generate test execution report"""
        print("\n" + "=" * 60)
        print("TEST EXECUTION REPORT")
        print("=" * 60)

        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r["status"] == "PASS")
        failed = sum(1 for r in self.test_results if r["status"] == "FAIL")
        errors = sum(1 for r in self.test_results if r["status"] == "ERROR")

        print(f"\nTotal Tests: {total}")
        print(f"Passed: {passed} ({(passed/total)*100:.1f}%)")
        print(f"Failed: {failed} ({(failed/total)*100:.1f}%)")
        print(f"Errors: {errors} ({(errors/total)*100:.1f}%)")

        print("\nDetailed Results:")
        print("-" * 60)
        for result in self.test_results:
            status_symbol = "✓" if result["status"] == "PASS" else "✗"
            print(f"{status_symbol} {result['test']}: {result['status']}")
            print(f"  Message: {result['message']}")
            print()


# Example usage (pseudo-code since we need actual login page)
if __name__ == "__main__":
    # Note: Replace with actual login page URL
    test_url = "https://example.com/login"

    print("""
    INSTRUCTIONS FOR RUNNING THIS TEST:
    1. Install Selenium: pip install selenium
    2. Download ChromeDriver matching your Chrome version
    3. Replace test_url with your actual login page URL
    4. Update element selectors (By.ID, By.CLASS_NAME) to match your page
    5. Run: python selenium_login_test.py
    """)

    # Uncomment to run actual tests:
    # automation = LoginTestAutomation(test_url)
    # automation.run_test_suite()