import user

admin = user.Admin("Rolo", "Lothbrook", 30, "rolo@loth.com")
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()
