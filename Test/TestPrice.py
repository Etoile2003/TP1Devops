import unittest

import pytest
from PriceService import *


class TestPrice(unittest.TestCase):
    def test_price(self):
        assert get_price() >=0
