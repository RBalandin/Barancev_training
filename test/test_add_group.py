# -*- coding: utf-8 -*-
from model.group import Group
from fixture.Application import Application
import pytest


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="asdfgh", header="asdfgh", footer="asdfgh"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


if __name__ == "__main__":
    pytest.main()
