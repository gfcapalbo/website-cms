# -*- coding: utf-8 -*-
# Copyright 2017 Simone Orsi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import tools

testing = tools.config.get('test_enable')


if not testing:
    # prevent these forms to be registered when running tests

    class ExampleEventForm(models.AbstractModel):
        """A test model form."""

        _name = 'cms.form.event.event'
        _inherit = 'cms.form'
        _form_model = 'event.event'
        _form_model_fields = ('name',)
        _form_required_fields = ('name',)
        _form_fields_order = ('name',)
        _form_display_mode = 'horizontal'

        custom = fields.Char()

        def _form_load_custom(
                self, form, main_object, fname, value, **req_values):
            """Load a custom default for the field 'custom'."""
            return req_values.get('custom', 'oh yeah!')

    class PartnerSearchForm(models.AbstractModel):
        """Partner model search form."""

        _name = 'cms.form.search.event.event'
        _inherit = 'cms.form.search'
        _form_model = 'event.event'
        _form_model_fields = ('name', 'talent_area_id', 'school_ids',
                              'school_year', )
        _form_display_mode = 'horizontal'

    @property
    def form_widgets(self):
        "associate talent area field to talent area widget"
        import pudb
        pudb.set_trace()
        res = super(ExampleEventForm, self).form_widgets
        res.update({
            'talent_area_id': 'cms_event_form.field_widget_talent_area_id'})
        return res


