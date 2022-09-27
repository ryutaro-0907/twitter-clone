from ....api.infra.utils.pass_hassing import Hash

pswd = "testingisawosome"
new_pswd = "testingisboroing"


def test_hash():
    hashed_pswd = Hash.get_password_hash(pswd)
    diff_pswd = Hash.verify_password(hashed_pswd, new_pswd)
    same_pswd = Hash.verify_password(hashed_pswd, pswd)

    assert same_pswd
    assert diff_pswd == False
