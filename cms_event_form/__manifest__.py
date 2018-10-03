# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'CMS event form',
    'summary': """ event search and view with cms_form""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Therp B.V.,Odoo Community Association (OCA)',
    'depends': [
        'website_event',
        'ppz_event',
        'ppz_partner',
        'cms_form',
    ],
    'data': [
        'templates/widgets.xml',
        'templates/assets.xml',
        'data/website_menu.xml',
        # 'forms/form_search_fields.xml',
        'forms/form_search_buttons.xml',
        'forms/form_search_results.xml',
    ]
}
