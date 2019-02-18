from odoo import models,fields, api

class coche(models.Model):
    _inherit = 'res.partner'
    name = fields.Char(string="name", required=True, help="Nombre de la pelicula")
    marca = fields.Char(string="marca", required=True, help="Nombre de la marca")
    modelo = fields.Char(string="modelo", required=True, help="Nombre del modelo")
    taller_id = fields.Many2one("taller1.taller", string="taller")


    @api.onchange('marca')
    def do_stuff(self):
        if self.marca == 'Peugeot':
            return {
                'warning':{
                    'title' : 'error',
                    'message' : 'asdsad'
                },
            }