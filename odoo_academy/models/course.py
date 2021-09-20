# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Titulo', required=True)
    
    description = fields.Text(string = 'Descripcion')
    
    level = fields.Selection(string='Level',
                            selection= [('principiante', 'Principiante'),
                                       ('intermedio', 'Intermedio'),
                                       ('avanzado', 'Avanzado')],
                            copy=False)
    active = fields.Boolean(string='Active', default=True)
    
    base_price = fields.Float(string='Base Price', default=0.00)
    
    additional_fee = fields.Float(string='Additional Fee', default=10.00)
    
    total_price = fields.Float(string='Total Price', readonly=True)
    
    sessions_ids = fields.One2many(comodel_name='academy.session',
                                 inverse_name='course_id',
                                 string='Sessions')
    
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0:
            raise UserError('El precio base no puede ser negativo.')
        self.total_price = self.base_price + self.additional_fee
    
    @api.constrains('additional_fee')
    def check_add_fee(self):
        for record in self:
            if record.additional_fee < 10:
                raise ValidationError('El costo adicional no puede ser menos de 10. Valor ingresado: %s' %record.additional_fee)
        