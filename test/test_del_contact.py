from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="", mobile="",
                               workphone="", fax="", email="", email2="",
                               email3="", homepage="", bday="", bmonth="", byear="", aday="",
                               amonth="", ayear="", address2="", phone2="", notes=""))
    app.contact.delete_first_contact()
