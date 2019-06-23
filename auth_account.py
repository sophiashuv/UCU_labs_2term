import auth

# Set up a test user and permission
auth.authenticator.add_user("admin", "1234qwer")
auth.authorizor.add_permission("add permission")
auth.authorizor.add_permission("permitted")
auth.authorizor.permit_user("add permission", "admin")
auth.authorizor.add_permission("add photo")
auth.authorizor.add_permission("add status")
auth.authorizor.permit_user("permitted", "admin")


class Editor:
    lst_users =[]
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "add permission": self.add_permission,
            "permittd": self.permitted,
            "add photo": self.add_photo,
            "add status": self.add_status,
            "register user": self.register_user,
            "all users": self.all_users,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
                Editor.lst_users.append(username)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def add_permission(self, permission):
        if self.username == 'admin' and self.is_permitted("add permission"):
            try:
                auth.authorizor.add_permission(permission)
            except auth.PermissionError:
                print('Permission is here')
        else:
            print("Permission isn't here")

    def permitted(self, username, permission):
        if self.username == 'admin' and self.is_permitted("permitted"):
            try:
                auth.authorizor.permit_user(permission, username)
            except auth.PermissionError:
                print('Permission not found')
        print("You can't do this")

    def register_user(self, username, password):
        try:
            auth.authenticator.add_user(username, password)
            Editor.lst_users.append(username)
            print("Hello "+str(username))
        except auth.PasswordTooShort:
            print("Tis password is too short")
        except auth.UsernameAlreadyExists:
            print("This username already exists")

    def add_photo(self):
        if self.is_permitted("add photo"):
            raise NotImplementedError
        else:
            print("It's forbidden")

    def add_status(self):
        if self.is_permitted("add status"):
            raise NotImplementedError
        else:
            print("It's forbidden")

    def all_users(self):
        for user in Editor.lst_users:
            print(user)

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
\tlogin\tLogin
\tregister user\tRegister a user
\tall users\tAll users
\tadd permission\tAdd permission
\tpermitted\tPermitted
\tadd photo\tAdd photo
\tadd status\tAdd status
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    try:
                        if answer == 'add permission':
                            self.add_permission(input('permission: ').lower())
                        elif answer == 'permitted':
                            self.permitted(input('username: ').lower(), input('permission: ').lower())
                        elif answer == 'register user':
                            self.register_user(input('username: ').lower(), input('password: ').lower())
                        else:
                            func()
                    except auth.PermissionError:
                        print('PermissionError occurred!')
        finally:
            print("Thanks for using the auth.py module!")


Editor().menu()

