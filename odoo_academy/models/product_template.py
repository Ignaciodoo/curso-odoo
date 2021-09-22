# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string='Uso como producto de Sesión',
                                       help='Selecciona esta casilla para usar esto como producto para costos de la sesión',
                                       default=False)
    
    