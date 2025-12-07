from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class AdmissionPortal(http.Controller):
    
    @http.route('/my/applications', type='http', auth='user', website=True)
    def my_applications(self, **kwargs):
        """
        Portal page for applicants to view their application
        """
        user = request.env.user

        applicant = request.env['admission.applicant'].search([
            ('user_id', '=', user.id)
        ], limit=1)
        
        if not applicant:
            applicant = request.env['admission.applicant'].search([
                ('email', '=', user.email)
            ], limit=1)
            
            if applicant and not applicant.user_id:
                applicant.user_id = user.id
        
        values = {
            'applicant': applicant,
            'page_name': 'my_applications',
            'user': user,
        }
        
        return request.render('zcundergrad_admission.portal_applicant_page', values)
    
    @http.route('/my/applications/update', type='http', auth='user', website=True, csrf=False)
    def update_application(self, **post):
        """
        Allow applicants to update their information from portal
        """
        user = request.env.user
        applicant = request.env['admission.applicant'].search([
            ('user_id', '=', user.id)
        ], limit=1)
        
        if not applicant:
            applicant = request.env['admission.applicant'].search([
                ('email', '=', user.email)
            ], limit=1)
        
        if applicant and post:
            # Update basic information
            update_fields = {}
            if 'phone' in post:
                update_fields['phone'] = post.get('phone')
            if 'mobile' in post:
                update_fields['mobile'] = post.get('mobile')
            if 'address' in post:
                update_fields['address'] = post.get('address')
            
            if update_fields:
                applicant.write(update_fields)
        
        return request.redirect('/my/applications')
