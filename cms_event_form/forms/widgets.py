# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import calendar
from odoo import models


class TalentAreaWidget(models.AbstractModel):

    _name = 'cms.form.widget.talent_area_id'
    _inherit = 'cms.form.widget.mixin'
    _w_template = 'cms_event_form.field_widget_talent_area_id'
    _w_css_class = 'divTable'

    # new properties of this particular widget
    _w_css_row_klass = 'divTableRow'
    _w_css_option_klass = 'divTableCell'

    def widget_init(self, form, fname, field, **kw):
        widget = super(TalentAreaWidget, self).widget_init(
            form, fname, field, **kw)
        widget.w_comodel = self.env[widget.w_field['relation']]
        widget.w_domain = widget.w_field.get('domain', [])
        return widget

    @property
    def w_option_items(self):
        return self.w_comodel.search(self.w_domain)

    @property
    def w_css_klass(self):
        return self._w_css_klass

    @property
    def w_css_option_klass(self):
        return self._w_css_option_klass

    @property
    def w_css_row_klass(self):
        return self._w_css_row_klass

class SessionIdWidget(models.AbstractModel):

    _name = 'cms.form.widget.session_ids'
    _inherit = 'cms.form.widget.mixin'
    _w_template = 'cms_event_form.field_widget_session_ids'

    @property
    def w_option_items(self):
        return list(calendar.day_name)



