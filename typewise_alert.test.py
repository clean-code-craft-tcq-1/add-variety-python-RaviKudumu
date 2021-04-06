import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
      self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    #   self.assertTrue(typewise_alert.infer_breach(101, 50, 100) == 'TOO_HIGH')
    #   self.assertTrue(typewise_alert.infer_breach(60, 50, 100) == 'NORMAL')
    #
    # def test_classify_temperature_breach(self):
    #     self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 36) == 'TOO_HIGH')
    def test_check_and_alert(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 40) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', -10) == 'TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 4) == 'NORMAL')

# check_and_alert('TO_EMAIL', temperature_limits['PASSIVE'], 0)
# check_and_alert('TO_EMAIL', temperature_limits['HI_ACTIVE'], -2)
# check_and_alert('TO_EMAIL', temperature_limits['MED_ACTIVE'], 41)
if __name__ == '__main__':
  unittest.main()
