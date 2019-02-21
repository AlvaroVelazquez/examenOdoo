from odoo import models,fields, api

class taller(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'taller1.taller'
    direccion = fields.Char(string="direccion", help="Nombre de la calle", compute='_compute_name')
    coche_ids = fields.One2many("res.partner", "taller_id", string="coches")
    mecanico_ids = fields.One2many("base.entidad", "taller_id", string="mecanicos")


    @api.multi
    def _compute_name(self):
        for taller in self:
            taller.direccion = "papito"
            

