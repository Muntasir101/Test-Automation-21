from Tutorial_Ninja import register_account, login


def end_to_end_all():
    register_account.register_testCase_valid()
    register_account.register_testCase_firstName()
    register_account.register_testCase_lastName()

    login.login_testCase_valid()
    login.login_testCase_invalid()


end_to_end_all()
