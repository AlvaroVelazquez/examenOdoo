from odoo import models,fields, api

class mecanico(models.Model):
    #Extension
    _inherit = 'base.entidad'
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del mecanico")
    seguro = fields.Boolean(string="seguro")
    pais_id = fields.Many2one("taller1.pais", string="pais")
    taller_id = fields.Many2one("taller1.taller", string="taller")
