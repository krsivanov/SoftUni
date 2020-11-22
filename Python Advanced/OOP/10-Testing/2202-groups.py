class Person:
    id_counter = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = Person.id_counter
        Person.id_counter += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"Person {self.id}: {self.name} {self.surname}"

    def __str__(self):
        return self.name + ' ' + self.surname


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, item):
        return self.people[item].__repr__()

    def __add__(self, other):
        return Group(self.name, self.people + other.people)

    def __str__(self):
        return f"Group {self.name} with members{', '.join(str(x) for x in self.people)}"


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        Person.id_counter = 0
        self.person_1 = Person("Ines", "Ivanova")

    def test_custom_repr(self):
        result = repr(self.person_1)
        self.assertIn('Ines', result)
        self.assertNotIn("Iness", result)
        self.assertEqual(result, "Person 0: Ines Ivanova")

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertIn("Ines", result)
        self.assertNotIn("Person", result)
        self.assertEqual(result, "Ines Ivanova")

    def test_autoIncremented_id(self):
        current_id_counter = Person.id_counter
        person_2 = Person('2', '2')

        self.assertEqual(current_id_counter, 1)
        self.assertEqual(person_2.id, 1)
        self.assertEqual(Person.id_counter, 2)

    def test_custom_add(self):
        person_2 = Person("Test", "Testov")
        person_3 = self.person_1 + person_2
        self.assertEqual(person_3.name, "Ines")
        self.assertEqual(person_3.surname, 'Testov')

    def test_set_attributes(self):
        self.assertEqual(self.person_1.name, "Ines")
        self.assertEqual(self.person_1.surname, "Ivanova")


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Ines", "Ivanova")
        self.person_2 = Person('Second', "Person")
        self.group = Group('test', [self.person_1, self.person_2])

    def test_custom_len(self):
        self.assertEqual(len(self.group), 2)

    def test_custom_add(self):
        person_3 = Person('Third', 'Third')
        group_2 = Group('test2', [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_get_item(self):
        result = self.group[1]
        self.assertIn("Second", result)
        self.assertEqual(result, "Person 1: Second Person")

    def test_custom_get_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_custom_repr(self):
        result = repr(self.group)
        self.assertIn("Group", result)
        self.assertIn("Ines", result)
        self.assertIn("Second", result)
        self.assertNotIn("Third", result)
        self.assertEqual(result,"Group test with members Ines Ivanova, Second Person")

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn("Group", result)
        self.assertIn("Ines", result)
        self.assertIn("Second", result)
        self.assertNotIn('Third', result)
        self.assertEqual(result,"Group test with members Ines Ivanova, Second Person")


    def test_set_attributes(self):
        self.assertEqual(self.group.name, "test")
        self.assertEqual(len(self.group.people), 2)


if __name__ == "__main__":
    unittest.main()
