import os
import json
import tempfile
import unittest

from json_practice import (
	EXAMPLE_PEOPLE_JSON,
	load_people_from_string,
	remove_key_from_people,
	people_to_sorted_json,
	get_people_without_license,
	extract_emails,
	save_json_to_file,
	load_json_from_file,
)


class TestJsonPractice(unittest.TestCase):
	def setUp(self):
		self.data = {
			"people": [
				{
					"name": "John Smith",
					"phone": "615-555-7164",
					"emails": ["john.doe@example.com", "john@doe.com"],
					"has_license": False,
				},
				{
					"name": "Jane Doe",
					"phone": "615-555-7165",
					"emails": ["jane.doe@example.com", "jane@doe.com"],
					"has_license": True,
				},
			]
		}

	def test_load_people_from_string(self):
		parsed = load_people_from_string(EXAMPLE_PEOPLE_JSON)
		self.assertIsInstance(parsed, dict)
		self.assertIn("people", parsed)
		self.assertEqual(len(parsed["people"]), 2)
		self.assertIs(parsed["people"][0]["has_license"], False)
		self.assertIs(parsed["people"][1]["has_license"], True)

	def test_remove_key_from_people(self):
		result = remove_key_from_people(self.data, "phone")
		self.assertIsNot(result, self.data)
		self.assertIn("people", result)
		for original, updated in zip(self.data["people"], result["people"]):
			self.assertIn("phone", original)
			self.assertNotIn("phone", updated)

	def test_people_to_sorted_json(self):
		result_json = people_to_sorted_json(self.data)
		loaded = json.loads(result_json)
		self.assertEqual(loaded, self.data)
		self.assertIn("\n  \"people\": ", result_json)

	def test_get_people_without_license(self):
		non_licensed = get_people_without_license(self.data)
		self.assertEqual(len(non_licensed), 1)
		self.assertEqual(non_licensed[0]["name"], "John Smith")

	def test_extract_emails(self):
		emails = extract_emails(self.data)
		self.assertEqual(
			emails,
			[
				"john.doe@example.com",
				"john@doe.com",
				"jane.doe@example.com",
				"jane@doe.com",
			],
		)

	def test_save_and_load_json_file(self):
		with tempfile.TemporaryDirectory() as tmp:
			path = os.path.join(tmp, "people.json")
			save_json_to_file(self.data, path)
			loaded = load_json_from_file(path)
			self.assertEqual(loaded, self.data)


if __name__ == "__main__":
	unittest.main()