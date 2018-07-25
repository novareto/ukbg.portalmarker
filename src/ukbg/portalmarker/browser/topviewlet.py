from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalTop
from plone.app.layout.viewlets.interfaces import IPortalHeader
from plone import api as ploneapi
from uvc.api import api

api.templatedir('templates')

class PortalMarkerViewlet(api.Viewlet):
    api.context(Interface)
    api.viewletmanager(IPortalTop)

    def update(self):
        self.greetings = 'Hallo Welt'
	self.memberfullname = self.member_name_or_id()

    def member_name_or_id(self, ):
        """
        """
        if ploneapi.user.is_anonymous():
            return ''

        member = ploneapi.user.get_current()
        fullname = member.getProperty('fullname', '')

        if fullname:
            return fullname
        else:
            return member.getId()

