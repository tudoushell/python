import unittest
from Test import formatname as get_formatted_name
class Test(unittest.TestCase):
      def testname():
          name=get_formatted_name('a','asdf')
          self.assertEqual(name,'')
unittest.main()

# import unittest
# from name_function import get_formatted_name
# class NamesTestCase(unittest.TestCase):
#        def test_first_last_name(self):
#             formatted_name = get_formatted_name('janis', 'joplin')
#             self.assertEqual(formatted_name, '')
# unittest.main() 