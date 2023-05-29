from odoo import fields, models, _

class CreatePartnerMultiWizard(models.TransientModel):
    _name = 'create.partners.multi.wizard'

    names = fields.Char('Partner Names')
    country_id = fields.Many2one('res.country', 'Country')
    company_type = fields.Selection([
                                    ('person', 'Individual'),
                                    ('company', 'Company')],
        string='Company type',
        default='person',
    )

    def action_open_wizard(self):
        return {
            'name': _('Create Partners Wizard'),
            # 'name': 'Create Partners Wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'create.partners.multi.wizard',
            'target': 'new',
            'context': {'default_country_id': self.env.user.company_id.id},
        }

    def action_create_record(self):
        self.ensure_one()
        for name in self.names.split(","):
            self.env['res.partner'].create({
                'name': name,
                'company_type': self.company_type,
                'country_id': self.country_id.id,
            })
