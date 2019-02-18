from odoo import models,fields, api

class pais(models.Model):
    _name = 'taller1.pais'
    name = fields.Char(string="name", required=True, help="Nombre del pais")
    mecanico_ids = fields.One2many("taller1.mecanico", "taller_id", string="pais")