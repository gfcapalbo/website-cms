# -*- coding: utf-8 -*-
# Copyright 2017 Simone Orsi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import calendar
from datetime import datetime

from odoo import models
from odoo import tools
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

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
        form_title = ''
        form_results_per_page = 30
        form_buttons_template = 'cms_event_form.form_buttons'
        #form_fields_template = 'cms_event_form.form_fields'
        form_search_results_template = 'cms_event_form.form_search_results'

        # the search form did not have the cancel_url method
        def form_cancel_url(self, main_object=None):
            """URL to redirect to after click on "cancel" button."""
            if self.request.args.get('redirect'):
                # redirect overridden
                return self.request.args.get('redirect')
            main_object = main_object or self.main_object
            if main_object and 'website_url' in main_object:
                return main_object.website_url
            return self.request.referrer or '/'


        @property
        def form_widgets(self):
            "associate talent area field to talent area widget"
            res = super(EventSearchForm, self).form_widgets
            res.update({
                'talent_area_id': 'cms.form.widget.talent_area_id'})
            return res

        # add to the form class some support properties we will need in templates
        weekdays = list(calendar.day_name)
        DSDF = DEFAULT_SERVER_DATETIME_FORMAT
        dt = datetime

