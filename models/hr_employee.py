from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    # Campos adicionais específicos para Forte Facilities
    naturalidade = fields.Char(string="Naturalidade", groups="hr.group_hr_user")
    deficiency_type = fields.Char(string="Tipo de Deficiência", groups="hr.group_hr_user")
    race = fields.Selection([
        ('branca', 'Branca'),
        ('negra', 'Negra'),
        ('amarela', 'Amarela'),
        ('parda', 'Parda'),
        ('indigena', 'Indígena'),
        ('nao_informado', 'Não informado')
    ], string="Raça/Cor", groups="hr.group_hr_user")
    
    # Campo para CBO (Classificação Brasileira de Ocupações)
    cbo_code = fields.Char(string="Código CBO", groups="hr.group_hr_user")
    
    # Campos relacionados à admissão e exames médicos
    date_medical_exam = fields.Date(string="Data Exame Médico", groups="hr.group_hr_user")
    validity_medical_exam = fields.Integer(
        string="Validade Exame Médico (meses)", 
        groups="hr.group_hr_user"
    )
    next_medical_exam = fields.Date(
        string="Próximo Exame Médico", 
        compute="_compute_next_medical_exam",
        store=True,
        groups="hr.group_hr_user"
    )
    
    # Campos relacionados ao sindicato e contrato
    union_name = fields.Char(string="Sindicato Representante", groups="hr.group_hr_user")
    contract_type = fields.Selection([
        ('clt', 'CLT'),
        ('pj', 'Pessoa Jurídica'),
        ('estagio', 'Estágio'),
        ('temporario', 'Temporário'),
        ('autonomo', 'Autônomo'),
        ('outro', 'Outro')
    ], string="Tipo de Contrato", groups="hr.group_hr_user")
    
    # Campos para horário de trabalho e outros detalhes
    work_schedule = fields.Char(string="Horário", groups="hr.group_hr_user")
    education_level = fields.Selection([
        ('alfabetizado', 'Alfabetizado'),
        ('fundamental_incompleto', 'Fundamental Incompleto'),
        ('fundamental', 'Fundamental Completo'),
        ('medio_incompleto', 'Médio Incompleto'),
        ('medio', 'Médio Completo'),
        ('superior_incompleto', 'Superior Incompleto'),
        ('superior', 'Superior Completo'),
        ('pos_graduacao', 'Pós-Graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado')
    ], string="Grau de Instrução", groups="hr.group_hr_user")
    
    # Campos para controle de alteração de cargo
    job_change_date = fields.Date(string="Data Alteração do Cargo", groups="hr.group_hr_user")
    
    @api.depends('date_medical_exam', 'validity_medical_exam')
    def _compute_next_medical_exam(self):
        """Calcula a data do próximo exame médico com base na data do último
        exame e sua validade em meses."""
        for employee in self:
            if employee.date_medical_exam and employee.validity_medical_exam:
                next_date = fields.Date.from_string(employee.date_medical_exam)
                next_date = next_date.replace(
                    year=next_date.year + int(employee.validity_medical_exam / 12),
                    month=next_date.month + (employee.validity_medical_exam % 12)
                )
                # Ajuste para meses com menos dias
                while True:
                    try:
                        employee.next_medical_exam = fields.Date.to_string(next_date)
                        break
                    except ValueError:
                        next_date = next_date.replace(day=next_date.day - 1)
            else:
                employee.next_medical_exam = False