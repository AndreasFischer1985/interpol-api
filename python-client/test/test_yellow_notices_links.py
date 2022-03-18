"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.yellow_notices_links_last import YellowNoticesLinksLast
from deutschland.interpol.model.yellow_notices_links_next import YellowNoticesLinksNext
from deutschland.interpol.model.yellow_notices_links_self import YellowNoticesLinksSelf

from deutschland import interpol

globals()["YellowNoticesLinksLast"] = YellowNoticesLinksLast
globals()["YellowNoticesLinksNext"] = YellowNoticesLinksNext
globals()["YellowNoticesLinksSelf"] = YellowNoticesLinksSelf
from deutschland.interpol.model.yellow_notices_links import YellowNoticesLinks


class TestYellowNoticesLinks(unittest.TestCase):
    """YellowNoticesLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testYellowNoticesLinks(self):
        """Test YellowNoticesLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = YellowNoticesLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()