import unittest

import pytest
from PriceService import *


class TestPrice(unittest.TestCase):
    def test_price(self):
        assert getPrice() >=0
