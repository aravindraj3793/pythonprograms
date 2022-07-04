def admin_permission_required(fn):
    def inner_fn(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("Permission Denied")
        else:
            return fn(*args, **kwargs)
        return inner_fn()


class User:
    def setuser(self, username, role):
        self.username = username
        self.role = role

    def printdetails(self):
        print(self.username, self.role)


class Addcourse:
    @admin_permission_required
    def setcourse(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def printdetails(self):
        print(self.user, self.course_name)


class Addbatch:
    @admin_permission_required
    def setbatch(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.batchcode = kwargs.get("batchcode")
        self.course = kwargs.get("course")

    def printdetails(self):
        print(self.user, self.batchcode, self.course)


usr = User()
usr.setuser("rahul", "staff")

crse = Addcourse()
crse.setcourse(user=usr, course_name="django")

batch = Addbatch()
batch.setbatch(user=usr, batch_code="D1234", course=crse)
