from odoo import models, fields, api

class EducationHistory(models.Model):
    _name = 'education.history'
    _description = 'Education History'
    
    applicant_id = fields.Many2one(
        'admission.applicant', 
        string='Applicant', 
        required=True
    )
    institution_name = fields.Char(string='Institution Name', required=True)
    qualification = fields.Char(string='Qualification', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    grade = fields.Float(string='Final Grade')
    document = fields.Binary(string='Certificate/Document')