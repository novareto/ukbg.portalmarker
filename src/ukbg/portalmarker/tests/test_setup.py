# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ukbg.portalmarker.testing import UKBG_PORTALMARKER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ukbg.portalmarker is properly installed."""

    layer = UKBG_PORTALMARKER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ukbg.portalmarker is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ukbg.portalmarker'))

    def test_browserlayer(self):
        """Test that IUkbgPortalmarkerLayer is registered."""
        from ukbg.portalmarker.interfaces import (
            IUkbgPortalmarkerLayer)
        from plone.browserlayer import utils
        self.assertIn(IUkbgPortalmarkerLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = UKBG_PORTALMARKER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ukbg.portalmarker'])

    def test_product_uninstalled(self):
        """Test if ukbg.portalmarker is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ukbg.portalmarker'))

    def test_browserlayer_removed(self):
        """Test that IUkbgPortalmarkerLayer is removed."""
        from ukbg.portalmarker.interfaces import \
            IUkbgPortalmarkerLayer
        from plone.browserlayer import utils
        self.assertNotIn(IUkbgPortalmarkerLayer, utils.registered_layers())
