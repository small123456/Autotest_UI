from common.base_page import BasePage


class CreateVM(BasePage):


    username_input = "xpath => //*[@id='txtUserName']"

    password_input = "xpath => //*[@id='txtUserPwd']"


    def input_username(self,username):

        self.input(self.username_input,username)
        self.mark_color(self.username_input)

    def input_password(self,password):

        self.input(self.password_input,password)


