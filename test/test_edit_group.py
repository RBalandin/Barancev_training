from model.group import Group


def test_edit_group(app):
    app.group.edit(Group(name="qwerty", header="asdfgh", footer="zxczxczxc"))
