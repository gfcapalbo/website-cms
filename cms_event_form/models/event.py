# -*- coding: utf-8 -*-
# Copyright 2017 Simone Orsi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import tools

testing = tools.config.get('test_enable')


if not testing:
    # prevent these forms to be registered when running tests

    class EventSearchForm(models.AbstractModel):
        """Partner model search form."""

        _name = 'cms.form.search.event.event'
        _inherit = 'cms.form.search'
        _form_model = 'event.event'
        _form_model_fields = ('name', 'talent_area_id', 'school_ids',
                              'school_year', )
        _form_display_mode = 'vertical'
        form_title = 'Search current activities'

    @property
    def form_widgets(self):
        "associate talent area field to talent area widget"
        res = super(EventSearchForm, self).form_widgets
        res.update({
            'talent_area_id': 'cms_event_form.field_widget_talent_area_id'})
        return res
