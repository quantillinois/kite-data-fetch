"""
Simple unit tests for the utilities module.
"""

import unittest
import utils
import uuid
import os


class TestUtilities(unittest.TestCase):
    """Tests the Utilities Module"""

    def test_read_env_success(self):
        """Tests if the environment reading succeeds for a
        variable that is set by script.
        """
        # generates a random key value pair using uuid
        random_text = str(uuid.uuid4())
        random_env = str(uuid.uuid4())
        # set the key value pair to the env
        os.environ[random_text] = random_env
        # assert that the key value pair is accurate when read.
        self.assertEqual(
            utils.read_env(random_text),
            random_env,
            msg="The read_env function should be able to read from the env.",
        )

    def test_read_env_failure(self):
        """Tests if the environment reading
        fails for a non existent variable
        """
        # generate random text with the uuid function, which is
        # sure to not exist in the environment.
        random_text = str(uuid.uuid4())
        # check if the LookupError is raised.
        self.assertRaises(LookupError, utils.read_env, random_text)
