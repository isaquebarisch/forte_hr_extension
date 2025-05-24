{
    "name": "Forte HR Extensions",
    "version": "14.0.1.0.0",
    "category": "Human Resources",
    "author": "Forte Conceito e Facilities",
    "website": "https://www.fortefacilities.com.br",
    "license": "AGPL-3",
    "depends": [
        "hr",
        "l10n_br_hr",
    ],
    "data": [
        "views/hr_employee_view.xml",
        "security/ir.model.access.csv",
        "data/hr_employee_data.xml",
    ],
    "installable": True,
    "application": False,
    "summary": "Extensões de RH específicas para Forte Conceito e Facilities",
    "description": """
        Este módulo estende as funcionalidades de RH para incluir campos adicionais 
        específicos para a Forte Conceito e Facilities, como CBO, sindicato, 
        data de exame médico, validade do exame e outros.
    """,
}