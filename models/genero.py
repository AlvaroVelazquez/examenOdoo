from odoo import models,fields, api

class genero(models.Model):
    
    name = fields.Char(string="name", required=True, help="Nombre del genero")
    direccion = fields.Char(string="direccion", help="Nombre de la calle")
    coche_ids = fields.One2many("res.partner", "taller_id", string="coches")
    mecanico_ids = fields.One2many("base.entidad", "taller_id", string="mecanicos")



