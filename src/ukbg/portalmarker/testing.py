# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ukbg.portalmarker


class UkbgPortalmarkerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ukbg.portalmarker)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ukbg.portalmarker:default')


UKBG_PORTALMARKER_FIXTURE = UkbgPortalmarkerLayer()


UKBG_PORTALMARKER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UKBG_PORTALMARKER_FIXTURE,),
    name='UkbgPortalmarkerLayer:IntegrationTesting'
)


UKBG_PORTALMARKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UKBG_PORTALMARKER_FIXTURE,),
    name='UkbgPortalmarkerLayer:FunctionalTesting'
)


UKBG_PORTALMARKER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UKBG_PORTALMARKER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='UkbgPortalmarkerLayer:AcceptanceTesting'
)
