# Write a function that provides an efficient look up of whether the user is in a group.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # recursively search for user and if not in group open group in group until no user nor group in group

    if user in group.get_users():
        return True

    elif not group.get_groups():
        return False

    else:
        for group_name in group.get_groups():
            if is_user_in_group(user, group_name) is True:
                return True

    return False


if __name__ == '__main__':
    # create groups
    parent_group = Group("parent_group")
    child_group_1 = Group("child_group_1")
    sub_child_group_1 = Group("subchild_group_1")
    sub_child_group_2 = Group("subchild_group_2")
    sub_child_group_3 = Group("subchild_group_3")

    # create and add users
    sub_child_user_1 = "sub_child_user_1"
    sub_child_group_1.add_user(sub_child_user_1)
    sub_child_user_2 = "sub_child_user_2"
    sub_child_group_2.add_user(sub_child_user_1)
    sub_child_user_3 = "sub_child_user_3"
    sub_child_group_1.add_user(sub_child_user_3)
    parent_user_1 = "parent_user_1"
    parent_group.add_user(parent_user_1)

    # add groups to groups
    child_group_1.add_group(sub_child_group_1)
    child_group_1.add_group(sub_child_group_2)
    child_group_1.add_group(sub_child_group_3)
    parent_group.add_group(child_group_1)

    """
    Group Structure:
    ├── parent_group/ parent_user_1
    │   ├── child_group_1/
    │   │   ├── sub_child_group_1/ sub_child_user_1, sub_child_user_3
    │   │   ├── sub_child_group_2/ sub_child_user_2
    │   │   ├── sub_child_group_3/
    """

    print(is_user_in_group(sub_child_user_1, parent_group))
    # expected: True

    print(is_user_in_group(parent_user_1, parent_group))
    # expected True

    print(is_user_in_group(parent_user_1, child_group_1))
    # expected False

    print(is_user_in_group('12345', parent_group))
    # expected False

