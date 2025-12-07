from odoo import models, fields, api

class AdmissionApplicant(models.Model):
    _name = 'admission.applicant'
    _inherit = ['portal.mixin']
    _description = 'Admission Applicant'
    
    # Personal Information
    name = fields.Char(string='Full Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    nationality = fields.Many2one('res.country', string='Nationality')
    
    # Contact Details
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    address = fields.Text(string='Full Address')
    
    # Emergency Contact
    emergency_contact_name = fields.Char(string='Emergency Contact Name')
    emergency_contact_phone = fields.Char(string='Emergency Contact Phone')
    emergency_contact_relation = fields.Char(string='Relationship')
    
    # Academic History
    education_history_ids = fields.One2many(
        'education.history', 
        'applicant_id', 
        string='Education History'
    )
    
    # Application Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')
    
    # O-Auth Integration
    oauth_uid = fields.Char(string='OAuth UID')
    oauth_provider = fields.Char(string='OAuth Provider')