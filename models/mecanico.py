from odoo import models,fields, api

class mecanico(models.Model):
    _name = 'taller1.mecanico'
    name = fields.Char(string="name", required=True, help="Nombre del mecanico")
    apellidos = fields.Char(string="name", required=True, help="Apellidos del mecanico")
    pais_id = fields.Many2one("taller1.taller", string="pais")
    taller_id = fields.Many2one("taller1.taller", string="taller")