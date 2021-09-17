# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'Summary': """App de Academia para entrenamiento en Odoo""",
    
    'description': """
    Modulo de academia para gestionar entrenamiento:
    - cursos
    - sesiones
    - asistentes""",
    
    'author': 'Ignacio',
    
    'website': 'http://www.Odoo.com/',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}
