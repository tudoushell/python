class User():
    def __init__(self,name,privileges):
        self.name=name
        self.privileges=privileges
    def current_user(self):
        print("当前用户名为 "+self.name+" 权限为："+str(self.privileges))

# class Privileges():
#     def __init__(self,name="can add post"):
#         self.name=name
#     def show(self):
#         print(self.name)
    
class Admin(User):
    def __init__(self,name,privileges):
        user_privileges=["can add post","can delete post","can ban user"]
        super().__init__(name,privileges)
        if privileges==1:
            self.users=user_privileges[0]
        elif privileges==2:
            self.users=user_privileges[1]
        else:
            self.users=user_privileges[2]
    def show_privileges(self):
       print("当前用户名为 "+self.name+" 权限为："+str(self.privileges)+" "+self.users)      
myuser=Admin("admin",2)   
myuser.show_privileges()

