# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.addons.website_sale.controllers.main import WebsiteSale

class Academy(http.Controller):
    
    @http.route('/academy/academy/', auth='user', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index',
                                   {'teachers': Teachers.search([])})

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })
    
    @http.route('/academy/new_teacher', type='http', auth="public", methods=['POST'], website=True)
    def new_teacher(self, **kwargs):
        print "TESTHCERMLKJF"
        return http.request.render('academy.teacher_submited', {})
    
    @http.route('/academy/teacher_submit', auth='public', website=True)
    def teacher_submit(self):
        return http.request.render('academy.teacher_submit', {}) 
    
    @http.route('/academy/teacher_submited', auth='public', website=True)
    def teacher_submited(self):
        return http.request.render('academy.teacher_submited', {}) 
    
class WebsiteForm(WebsiteForm):
    
    @http.route('/website_form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form(self, model_name, **kwargs):
        return super(WebsiteForm, self).website_form(model_name, **kwargs)
    
    def insert_record(self, request, model, values, custom, meta=None):
        return WebsiteForm.insert_record(self, request, model, values, custom, meta=meta)

# Ce faisant, limite l'accès au shop uniquement au user authentifié
class WebsiteSale(WebsiteSale):
    @http.route(auth='user')
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        return super(WebsiteSale, self).shop()
