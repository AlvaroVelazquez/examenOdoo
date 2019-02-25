from odoo import models,fields, api

class compania(models.Model):
    #Extension
    _inherit = 'base.entidad'
    videojuego_id = fields.Many2one("examen.videojuego", string="videojuego")
