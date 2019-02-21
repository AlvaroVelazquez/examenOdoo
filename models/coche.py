from odoo import models,fields, api

class coche(models.Model):
    #Extension
    _inherit = 'res.partner'
    name = fields.Char(string="name", required=True, help="Nombre de la pelicula")
    marca = fields.Char(string="marca", help="Nombre de la marca", compute='afun')
    modelo = fields.Char(string="modelo", required=True, help="Nombre del modelo")
    fechaSalida = fields.Date(string="fechaSalida")
    fechaEntrada = fields.Date(string="fechaEntrada")
    tiempo = fields.Date(string="duracion");
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
    

    @api.one
    def generate_record_name(self):
        self.modelo = '307'

    @api.depends('modelo')
    def afun(self):
        self.marca = self.modelo
        
    
    