# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.Application import Application
import pytest


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Tot", middlename="Samiy", lastname="Chelovek", nickname="Pchel",
                               title="CEO", company="Mashup", address="Lenin street", home="111", mobile="88005553535",
                               workphone="+790990900090", fax="27438567", email="q23984765@mail.ru", email2="jefn",
                               email3="sedjf", homepage="sodeifj", bday="12", bmonth="July", byear="1990", aday="17",
                               amonth="February", ayear="1991", address2="awsrg", phone2="sardfg", notes="awer"))
    app.session.logout()


if __name__ == "__main__":
    pytest.main()
