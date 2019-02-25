from odoo import models,fields, api

class consola(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'examen.consola'
    videojuego_ids = fields.One2many("base.entidad", "consola_id", string="videojuegos")


   
            

