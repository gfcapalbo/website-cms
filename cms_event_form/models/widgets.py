# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class TalentAreaWidget(models.AbstractModel):

    _name = 'widget_talent_area'
    _inherit = 'cms.form.widget.image'
    _w_template = 'cms_event_form.widget_talent_area'
    _w_css_class = 'talent-area'
