from common.base_page import BasePage


class DeleteVM(BasePage):


    username_input = "xpath => //*[@id='txtUserName']"

    password_input = "xpath => //*[@id='txtUserPwd']"


    def clear_username(self):

        self.clear(self.username_input)
        self.mark_color(self.username_input)

    def clear_password(self):

        self.clear(self.password_input)