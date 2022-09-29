from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.creation(Group(name="test"))
    app.group.edit(Group(name="qwerty", header="asdfgh", footer="zxczxczxc"))
