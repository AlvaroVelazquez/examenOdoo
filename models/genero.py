from odoo import models,fields, api

class genero(models.Model):
    
    name = fields.Char(string="name", required=True, help="Nombre del genero")
    videojuegos_ids = fields.One2many("genero_id", string="videojuegos")



