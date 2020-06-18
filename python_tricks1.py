# Check multiple Test Cases at once
# using assert_equal()

from nose.tools import assert_equal

# write function
def addition(a, b):
    return a + b

# Create a testing class
class SolutionTest():
    def test(self, sol):
        assert_equal(sol(2, 4), 6)
        assert_equal(sol(10, 14), 24)
        print('All Test Cases passed')

# Run Tests
ob = SolutionTest()
ob.test(addition)