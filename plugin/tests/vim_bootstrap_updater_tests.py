import unittest
import vim_bootstrap_updater as sut


@unittest.skip("Don't forget to test!")
class VimBootstrapUpdaterTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_bootstrap_updater_example()
        self.assertEqual("Happy Hacking", result)
