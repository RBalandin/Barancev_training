from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.creation(Group(name="test", header="", footer=""))
    app.group.delete_first_group()
