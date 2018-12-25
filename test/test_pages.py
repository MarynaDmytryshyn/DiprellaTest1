import allure


class TestPages(object):
     @allure.title("Verify the Login Page")
     @allure.description_html("Verifying <b>Login Page</b> that it contains the required for the testing elements")
     def test_login_page_elements(self):
         login_page = self.home.click_on_enter_button()
         with allure.step("Check that Diprella logo is present on the page and displayed"):
             assert login_page.diprella_logo.is_displayed(),'Diprella logo is displayed'
         with allure.step("Check that Signup button is present on the page and displayed"):
             assert login_page.enter_regisration_button.is_displayed(), 'Signup button is displayed'
         with allure.step("Check that Username field is present on the page and displayed"):
             assert login_page.username_input.is_displayed(), 'Username field is displayed'
         with allure.step("Check that Password field is present on the page and displayed"):
             assert login_page.password_input.is_displayed(), 'Password field is displayed'
         with allure.step("Check that Facebook login button is present on the page and displayed"):
             assert login_page.fb_login_button.is_displayed(), 'Facebook login button is displayed'
         with allure.step("Check that Google+ login button is present on the page and displayed"):
             assert login_page.google_login_button.is_displayed(), 'Google+ login button is displayed'
         with allure.step("Check that Linkedin login button is present on the page and displayed"):
             assert login_page.in_login_button.is_displayed(), 'Linkedin login button is displayed'
         with allure.step("Check that Login button is present on the page and displayed"):
             assert login_page.login_button.is_displayed(), 'Login button is displayed'

     @allure.title("Verify the Signup Page")
     @allure.description_html("Verifying <b>Login Page</b> that it contains the required for the testing elements")
     def test_signup_page_elements(self, user_information):
         signup_page = self.home.click_on_reg_button()
         name, surname, email, password = user_information
         workspace_page = signup_page.enter_name(name) \
               .enter_surname(surname) \
               .enter_email(email) \
               .enter_password(password) \
               .click_on_terms_checkbox() \
               .click_on_registration_button()
         with allure.step("Check that Library menu is present on the page and displayed"):
             assert workspace_page.library_menu.is_displayed(), 'Library menu is available'
         with allure.step("Check that Footer is present on the page and displayed"):
             assert workspace_page.footer.is_displayed(), 'Footer is displayed'
         with allure.step("Check that Language selector is present on the page and displayed"):
             assert workspace_page.language_selector.is_displayed(), 'Language selector is displayed'
         with allure.step("Check that Donate button is present on the page and displayed"):
             assert workspace_page.donate_button.is_displayed(), 'Danate button is displayed'
         with allure.step("Check that Contact us section is present on the page and displayed"):
             assert workspace_page.contact_us.is_displayed(), 'Contact us section is displayed'



     @allure.title("Verify the User Workspace Page")
     @allure.description_html("Verifying <b>Login Page</b> that it contains the required for the testing elements")
     def test_login_with_correct_creds(self, correct_credentials):
         login_page = self.home.click_on_enter_button()
         login_page.username_input.click()
         username, password = correct_credentials
         workspace_page = login_page.enter_username(username) \
             .enter_password(password) \
             .click_on_login_button()

         with allure.step("Check that Diprella logo is present on the page and displayed"):
             assert workspace_page.diprella_logo.is_displayed(), 'Diprella logo is displayed'
         with allure.step("Check that Courses search is present on the page and displayed"):
             assert workspace_page.courses_search.is_displayed(), 'Courses search field is displayed'
         with allure.step("Check that Instrucctor menu is present on the page and displayed"):
             assert workspace_page.instructor_menu.is_displayed(), 'Instructor menu is available'
         with allure.step("Check that Home tab is present on the page and displayed"):
             assert workspace_page.home_tab.is_displayed(), 'Home tab is displayed'
         with allure.step("Check that Bookmarks is present on the page and displayed"):
             assert workspace_page.bookmarks_tab.is_displayed(), 'Bookmarks tab is available'
         with allure.step("Check that Profile tab is present on the page and displayed"):
             assert workspace_page.profile_tab.is_displayed(), 'Profile tab is available'
         with allure.step("Check that Recommended courses is present on the page and displayed"):
             assert workspace_page.recommended_courses.is_displayed(), 'Recommended courses are available'
         with allure.step("Check that Popular courses is present on the page and displayed"):
             assert workspace_page.popular_courses.is_displayed(), 'Popular courses are available'

     @allure.title("Verify the Login Page with incorrect credentials")
     @allure.description_html("Verifying <b>Login Page</b> that it contains the required for the testing elements")
     def test_login_with_incorrect_creds(self, incorrect_credentials):
         login_page = self.home.click_on_enter_button()
         login_page.diprella_logo.click()
         self.home.click_on_enter_button()
         # facebook = login_page.fb_login_button.click()
         # facebook.click_not_now_button()
         with allure.step("Check that Diprella logo is present on the page and displayed"):
             assert login_page.diprella_logo.is_displayed(), 'Diprella logo is displayed'
         with allure.step("Check that Signup button is present on the page and displayed"):
             assert login_page.enter_regisration_button.is_displayed(), 'Signup button is displayed'
         with allure.step("Check that Username field is present on the page and displayed"):
             assert login_page.username_input.is_displayed(), 'Username field is displayed'
         with allure.step("Check that Password field is present on the page and displayed"):
             assert login_page.password_input.is_displayed(), 'Password field is displayed'
         with allure.step("Check that Facebook login is present on the page and displayed"):
             assert login_page.fb_login_button.is_displayed(), 'Facebook login button is displayed'
         with allure.step("Check that Google+ login button is present on the page and displayed"):
             assert login_page.google_login_button.is_displayed(), 'Google+ login button is displayed'
         with allure.step("Check that Linkedin login button is present on the page and displayed"):
             assert login_page.in_login_button.is_displayed(), 'Linkedin login button is displayed'
         with allure.step("Check that Login button is present on the page and displayed"):
             assert login_page.login_button.is_displayed(), 'Login button is displayed'
         login_page.username_input.click()
         username, password = incorrect_credentials
         login_page.enter_username(username) \
             .enter_password(password) \
             .click_on_login_button()

         with allure.step("Check that Forbidden message is present on the page and displayed"):
             assert login_page.error_message.is_displayed(), 'Forbidden message is displayed'
         with allure.step("Check that Enter your account is present on the page and displayed"):
             assert login_page.sign_in_text.is_displayed(), 'Enter your account'






        