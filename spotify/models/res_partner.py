
from unicodedata import name
from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError, ValidationError
import requests
import logging
import json



_logger = logging.getLogger(__name__)

QUERY_DOCUMENT = {
    'urls':{
            'tracks' : 'https://api.spotify.com/v1/search?q=genre:{genre}&type=track&market=ES&limit=1&offset=5'
    }                  
}

names = []
links = []
   

class ResPartner(models.Model):

    _inherit = 'res.partner' 
    genre_ids = fields.Many2many(
        'genres',
        string='generos',
        store = True
    )

    website = fields.Text(
        string='links recomendados'
    )

    def consult_tracks(self):
        links = []
        for rec in self:
            for i in rec.genre_ids:
                genero = str(i.name)
                url = QUERY_DOCUMENT['urls']['tracks'].format(genre=genero)
                token = self.env['ir.config_parameter'].sudo().get_param('token')
                headers = {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    #agregar aqui el token actual :0
                    'Authorization': 'Bearer BQAagX4VqrkgFx68x9kf3JmEO80HfIudbGWHbg-1lh_ZlKQrxNeb7ZOn_OLTz9OFFSEV02u4mAnI95CluGEdQM5gvZO27x6vVu_vpPGjtgQQPYVVr_yZovErglSl0Bd4KUZGSvepxL8JfB9eQCztoXXnLzZmzWxzOo_i7J_0MTIgxx-iLoSMMD5Xui0L_NA'                 
                    }
                result = requests.get(url, verify=False, headers=headers) 
                if result.status_code == 200:
                    result_json = result.json()
                    links.append(result_json['tracks']['items'][0]['external_urls']['spotify'])
                else:
                    raise ValidationError(f'Ha ocurrido un error :( {result.text} ')

        links = "// ".join(map(str, links))    
        self.update({  
                    'website': links
                 })                   
        return result
                
class Generes(models.Model):
    _name = 'genres' 


    name = fields.Char(
        string= "Genero"
    )

   
