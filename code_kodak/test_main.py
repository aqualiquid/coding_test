import unittest
from solution import Authorization

# Note: the class must be called Test
class Test(unittest.TestCase):
  def setUp(self):
    permissions = [
      { "role": "superuser", "name": "lock user account", "active": True },
      { "role": "superuser", "name": "unlock user account", "active": True },
      { "role": "superuser", "name": "purchase widgets", "active": False },
      { "role": "charger", "name": "view pick up locations", "active": True },
      { "role": "rider", "name": "view my profile", "active": True },
      { "role": "rider", "name": "scooters near me", "active": True },
    ]

    users = [
      { "id": 1, "name": "Anna Administrator", "roles": ["superuser"] },
      { "id": 2, "name": "Charles N. Charge", "roles": ["charger", "rider"] },
      { "id": 7, "name": "Ryder", "roles": ["rider"] },
      { "id": 11, "name": "Unregistered Ulysses", "roles": [] },
      { "id": 18, "name": "Tessa Tester", "roles": ["beta tester"] },
    ]

    self.authorization = Authorization(permissions, users)

  def test_list_permissions_returns_correct_permission_names_when_there_is_one_role(self):
    result = self.authorization.list_permissions(7)
    self.assertEqual("view my profile" in result, True)
    self.assertEqual("scooters near me" in result, True)
    self.assertEqual(len(result), 2)

  def test_check_permitted_returns_true_for_all_of_the_permissions_that_exist_for_the_user(self):
    self.assertEqual(self.authorization.check_permitted("view pick up locations", 2), True)
    self.assertEqual(self.authorization.check_permitted("view my profile", 2), True)
    self.assertEqual(self.authorization.check_permitted("scooters near me", 2), True)


# added by Wookyung An
  def test_roles_no_activate_permitted(self):
    self.assertEqual(self.authorization.list_permissions(18),[])

  def test_permission_not_active(self):
    self.assertFalse("purchase widgets" in self.authorization.list_permissions(1))


