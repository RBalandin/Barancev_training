from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="NeTot", middlename="NeSamiy", lastname="NeChelovek", nickname="NePchel",
                               title="NeCEO", company="AntiMashup", address="NeLenin street", home="222111", mobile="3535",
                               workphone="0090", fax="567", email="q5@mail.ru", email2="jn",
                               email3="sf", homepage="s", bday="2", bmonth="April", byear="2007", aday="2",
                               amonth="November", ayear="2000", address2="g", phone2="g", notes="a"))
