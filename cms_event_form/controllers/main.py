# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.addons.cms_form.controllers.main import SearchFormControllerMixin
from odoo.addons.cms_form.controllers.main import FormControllerMixin


class EventFormController(http.Controller, FormControllerMixin):
    """Event form controller."""

    @http.route([
        '/event/add',
        '/event/<model("event.event"):main_object>/edit',
    ], type='http', auth='user', website=True)
    def cms_form(self, main_object=None, **kw):
        """Handle a `form` route.
        """
        model = 'event.event'
        return self.make_response(
            model, model_id=main_object and main_object.id, **kw)


class EventListing(http.Controller, SearchFormControllerMixin):

    @http.route([
        '/event/event_list',
        '/event/event_list/page/<int:page>',
    ], type='http', auth="public", website=True)
    def market(self, **kw):
        model = 'event.event'
        return self.make_response(model, **kw)
