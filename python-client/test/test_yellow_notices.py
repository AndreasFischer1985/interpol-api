"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.red_notices_embedded import RedNoticesEmbedded
from deutschland.interpol.model.red_notices_query import RedNoticesQuery
from deutschland.interpol.model.yellow_notices_links import YellowNoticesLinks

from deutschland import interpol

globals()["RedNoticesEmbedded"] = RedNoticesEmbedded
globals()["RedNoticesQuery"] = RedNoticesQuery
globals()["YellowNoticesLinks"] = YellowNoticesLinks
from deutschland.interpol.model.yellow_notices import YellowNotices


class TestYellowNotices(unittest.TestCase):
    """YellowNotices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testYellowNotices(self):
        """Test YellowNotices"""
        # FIXME: construct object with mandatory attributes with example values
        # model = YellowNotices()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()