import mathlib
import pytest

class TestMathlib(object):
    def test_calc_add(self):
        total = mathlib.calc_add(5, 6)
        assert total == 11


    def test_calc_multiply(self):
        result = mathlib.calc_multiply(5, 6)
        assert result == 30


    def test_exception(self):
        with pytest.raises(SystemExit):
            mathlib.exception()


# allow the test to be called directly from the code in python
# pytest.main()
