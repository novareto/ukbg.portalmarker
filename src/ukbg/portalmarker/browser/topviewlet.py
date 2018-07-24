from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalTop
from plone.app.layout.viewlets.interfaces import IPortalHeader
from uvc.api import api

api.templatedir('templates')

class PortalMarkerViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IPortalTop)

    def update(self):
        self.greetings = 'Hallo Welt'
