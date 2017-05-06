# -*- coding: utf-8 -*-

'''
Created on 4 avr. 2017

@author: heifara
'''

from odoo import models, fields, api


class Courses(models.Model):
    _inherit = 'product.template'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")