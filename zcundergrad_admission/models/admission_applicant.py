from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AdmissionApplicant(models.Model):
    _name = 'admission.applicant'
    _inherit = ['portal.mixin']
    _description = 'Admission Applicant'
    _rec_name = 'name'
    
    # Link to portal user
    user_id = fields.Many2one(
        'res.users',
        string='Portal User',
        help='Link to portal user account'
    )
    
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

    # Portal access URL
    def _get_portal_url(self):
        """Get the portal URL for this applicant"""
        self.ensure_one()
        return '/my/applications'
    
    # Action methods for state transitions
    def action_submit(self):
        """Submit the application"""
        for applicant in self:
            if applicant.state == 'draft':
                applicant.state = 'submitted'
    
    def action_accept(self):
        """Accept the application"""
        for applicant in self:
            if applicant.state == 'under_review':
                applicant.state = 'accepted'
    
    def action_reject(self):
        """Reject the application"""
        for applicant in self:
            if applicant.state == 'under_review':
                applicant.state = 'rejected'
    
    def action_send_to_review(self):
        """Send application for review"""
        for applicant in self:
            if applicant.state == 'submitted':
                applicant.state = 'under_review'
    
    def action_reset_to_draft(self):
        """Reset application to draft"""
        for applicant in self:
            applicant.state = 'draft'
    
    @api.model
    def create(self, vals):
        """Override create to handle portal user linking"""
        # Check if email corresponds to an existing user
        if 'email' in vals:
            user = self.env['res.users'].search([('login', '=', vals['email'])], limit=1)
            if user:
                vals['user_id'] = user.id
        
        return super(AdmissionApplicant, self).create(vals)
    
    def write(self, vals):
        """Override write to handle portal user linking"""
        if 'email' in vals:
            user = self.env['res.users'].search([('login', '=', vals['email'])], limit=1)
            if user:
                vals['user_id'] = user.id
        
        return super(AdmissionApplicant, self).write(vals)from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class AdmissionApplicant(models.Model):
    _name = 'admission.applicant'
    _inherit = ['portal.mixin']
    _description = 'Admission Applicant'
    _rec_name = 'name'
    
    # Link to portal user
    user_id = fields.Many2one(
        'res.users',
        string='Portal User',
        help='Link to portal user account'
    )
    
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

    # Portal access URL
    def _get_portal_url(self):
        """Get the portal URL for this applicant"""
        self.ensure_one()
        return '/my/applications'
    
    # Action methods for state transitions
    def action_submit(self):
        """Submit the application"""
        for applicant in self:
            if applicant.state == 'draft':
                applicant.state = 'submitted'
    
    def action_accept(self):
        """Accept the application"""
        for applicant in self:
            if applicant.state == 'under_review':
                applicant.state = 'accepted'
    
    def action_reject(self):
        """Reject the application"""
        for applicant in self:
            if applicant.state == 'under_review':
                applicant.state = 'rejected'
    
    def action_send_to_review(self):
        """Send application for review"""
        for applicant in self:
            if applicant.state == 'submitted':
                applicant.state = 'under_review'
    
    def action_reset_to_draft(self):
        """Reset application to draft"""
        for applicant in self:
            applicant.state = 'draft'
    
    @api.model
    def create(self, vals):
        """Override create to handle portal user linking"""
        # Check if email corresponds to an existing user
        if 'email' in vals:
            user = self.env['res.users'].search([('login', '=', vals['email'])], limit=1)
            if user:
                vals['user_id'] = user.id
        
        return super(AdmissionApplicant, self).create(vals)
    
    def write(self, vals):
        """Override write to handle portal user linking"""
        if 'email' in vals:
            user = self.env['res.users'].search([('login', '=', vals['email'])], limit=1)
            if user:
                vals['user_id'] = user.id
        
        return super(AdmissionApplicant, self).write(vals)
