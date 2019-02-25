from odoo import models,fields, api

class videojuego(models.Model):
    name = fields.Char(string="name", required=True, help="Nombre del videojuego")
    precio = fields.integer(string="precio", help="precio del videojuego")
    num_ventas = fields.integer(string="ventas",  help="Numero de ventas")
    dinero_generado = fields.integer(string="dinero_generado", help="Dinero generado")
    captura = fields.Boolean(string="captura")
    saga_id = fields.Many2one("examen.saga", string="saga")
    compania_id = fields.Many2one("examen.compania", string="compania")
    genero_id = fields.Many2one("examen.genero", string="genero")
    consola_id = fields.Many2one("examen.consola", string="consola")    



    
    
    