"""
    Interpol Notices API

    Interpol Red, Yellow and UN Notices API  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.interpol.model.un_notice_detail_images_links_thumbnail import (
    UNNoticeDetailImagesLinksThumbnail,
)
from deutschland.interpol.model.un_notice_detail_links_images import (
    UNNoticeDetailLinksImages,
)
from deutschland.interpol.model.un_notice_detail_links_self import (
    UNNoticeDetailLinksSelf,
)

from deutschland import interpol

globals()["UNNoticeDetailImagesLinksThumbnail"] = UNNoticeDetailImagesLinksThumbnail
globals()["UNNoticeDetailLinksImages"] = UNNoticeDetailLinksImages
globals()["UNNoticeDetailLinksSelf"] = UNNoticeDetailLinksSelf
from deutschland.interpol.model.un_notice_detail_links import UNNoticeDetailLinks


class TestUNNoticeDetailLinks(unittest.TestCase):
    """UNNoticeDetailLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUNNoticeDetailLinks(self):
        """Test UNNoticeDetailLinks"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UNNoticeDetailLinks()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()