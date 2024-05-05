# see graphic in instructions for visual explanation of the permission and user data structures
class Authorization:
  def __init__(self, permissions, users):
    self.permissions = permissions
    self.users = users

# @rtype: list of strings
# @returns: a list of all the active permission names that the user with the corresponding user_id has
# @note: The order in which the permission names are returned is not important
# @example: listPermissions(1) ➡ ["View Orders", "Block User Account"] (purchased widgets not included since it is not active)
  def list_permissions(self, user_id):
    # TODO: fill this out!
    # initialize stored roles for the given user_id
    user_roles =[]

    for user in self.users:
      if user['id'] == user_id:
        user_roles = user['roles']
        break

    # return empty list if no users were found
    if not user_roles: return []

    granted =[]
    for role in user_roles:
      for perm in self.permissions:
        if perm['role'] == role and perm['active']:
          if perm['name'] not in granted:
            granted.append(perm['name'])
    return granted


# @rtype: boolean value
# @returns: true or false based on if the user with the corresponding user_id has the role that corresponds with the specific permission_name and that particular permission is active
# @example: Example (Based on data from graphic)
# checkPermitted("scooters near me", 2) ➡ true
# checkPermitted("scooters near me", 1) ➡ false
  def check_permitted(self, permission_name, user_id):
    # TODO: fill this out!
    permissions = self.list_permissions(user_id)
    return permission_name in permissions
