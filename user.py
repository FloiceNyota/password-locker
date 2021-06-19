class User: # generates new instance of user
    user_list = [] #data structure

    def __init__(self,user_name,password): #constructor method
        self.user_name = user_name
        self.password = password

    def save_user(self):

        User.user_list.append(self)    



