from odoo import models,fields, api

class taller(models.Model):
    _name = 'taller1.taller'
    name = fields.Char(string="name", required=True, help="Nombre del taller")
    direccion = fields.Char(string="marca", required=True, help="Nombre de la calle")
    coche_ids = fields.One2many("res.partner", "taller_id", string="coches")
    mecanico_ids = fields.One2many("taller1.mecanico", "taller_id", string="mecanicos")