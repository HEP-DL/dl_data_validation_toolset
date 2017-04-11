from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.data_tests.labels import LabelTests

class TestDl_CLI(base_unittest.BaseTestCase):

  def test_label_existence(self):
    label_test = LabelTests('somefile.h5')
    self.mock_file['label/type']=[[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    label_test.go()