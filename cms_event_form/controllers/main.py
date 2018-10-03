# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.addons.cms_form.controllers.main import SearchFormControllerMixin


class EventListing(http.Controller, SearchFormControllerMixin):

    @http.route([
        '/event/event_list',
    ], type='http', auth="public", website=True)
    def market(self, **kw):
        model = 'event.event'
        return self.make_response(model, **kw)
