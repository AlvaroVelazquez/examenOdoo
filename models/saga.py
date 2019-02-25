from odoo import models,fields, api

class saga(models.Model):
    name = fields.Char(string="name", required=True, help="Nombre de la saga")
    videojuego_ids = fields.One2many("saga_id", string="saga")