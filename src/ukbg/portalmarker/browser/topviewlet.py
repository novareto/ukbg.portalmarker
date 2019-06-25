from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalTop
from plone.app.layout.viewlets.interfaces import IPortalHeader
from nva.contentboxes.browser.viewlets import ContentBoxViewlet
from plone import api as ploneapi
from uvc.api import api

api.templatedir('templates')

class PortalMarkerViewlet(ContentBoxViewlet):
    api.context(Interface)
    api.viewletmanager(IPortalTop)


    def memberdata(self):
        self.memberfullname = self.member_name_or_id()
        self.memberfolder = self.memberfolder()
        self.memberprefs = self.memberprefs()
        self.userprofile = self.userprofile()

    def memberfolder(self):
        if not ploneapi.user.is_anonymous():
            userid = ploneapi.user.get_current().id
            portalobj = ploneapi.portal.get()
            members = getattr(portalobj, 'Members', None)
            if members:
                memberfolder = getattr(members, userid, None)
                if memberfolder:
                    return "%s/Members/%s" %(ploneapi.portal.get().absolute_url(), userid)
            return None

    def memberprefs(self):
        return ploneapi.portal.get().absolute_url() + '/@@personal-preferences'

    def userprofile(self):
        return ploneapi.portal.get().absolute_url() + '/@@userprofileform'

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

