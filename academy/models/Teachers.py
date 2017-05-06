# -*- coding: utf-8 -*-

'''
Created on 4 avr. 2017

@author: heifara
'''
from odoo import models, fields, api, exceptions

class Teachers(models.Model):
    _name = 'academy.teachers'
    _inherit = ['mail.thread', 'ir.needaction_mixin', 'utm.mixin', 'rating.mixin', 'website.published.mixin']

    name = fields.Char()
    biography = fields.Html("biography")
    bio = fields.Char()
    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")

    def _compute_website_url(self):
        for teacher in self:
            teacher.website_url = "/academy/%s" % (teacher.id)
            
    @api.model
    def message_get_reply_to(self, res_ids, default=None):
        res = {}
        for res_id in res_ids:
            res[res_id] = super(Teachers, self).message_get_reply_to([res_id])[res_id]
        return res