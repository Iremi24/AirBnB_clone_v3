#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
        """Tests for the BaseModel class."""

            def setUp(self):
                        """Set up for each test."""
                                self.model = BaseModel()

                                    def test_instance_creation(self):
                                                """Test if an instance of BaseModel is created."""
                                                        self.assertIsInstance(self.model, BaseModel)

                                                            def test_save_method(self):
                                                                        """Test the save method."""
                                                                                old_updated_at = self.model.updated_at
                                                                                        self.model.save()
                                                                                                self.assertNotEqual(old_updated_at, self.model.updated_at)

                                                                                                    def test_to_dict_method(self):
                                                                                                                """Test the to_dict method."""
                                                                                                                        model_dict = self.model.to_dict()
                                                                                                                                self.assertEqual(model_dict['__class__'], 'BaseModel')
                                                                                                                                        self.assertEqual(model_dict['id'], self.model.id)

                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                unittest.main()
