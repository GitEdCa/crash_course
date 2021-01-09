import user_m
import admin


admin = user_m.Admin("Rolo as", "Lothbrook", 30, "rolo@loth.com")
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()
