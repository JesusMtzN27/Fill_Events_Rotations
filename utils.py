from sqlalchemy import cast, String
from sqlalchemy.orm import Session

def convert_payroll_id_to_string(employee):
    """
    Convierte el campo payrollNumberBoss_id de un empleado a string.
    Si el campo es de tipo entero (BigInt), lo convierte a string.
    """
    payroll_id = employee.payrollNumberBoss_id
    
    # Convertir a string si es un número entero
    if isinstance(payroll_id, int):
        return str(payroll_id)
    # Si ya es una cadena (VARCHAR), no se realiza ninguna acción
    elif isinstance(payroll_id, str):
        return payroll_id
    # Para cualquier otro tipo, se convierte a string
    return str(payroll_id)

def get_employees(db_session: Session, tenant_id: str):
    """
    Obtiene todos los empleados activos para un tenant.
    """
    from models.employee import EmployeeTenant  # Asegúrate de que la ruta sea correcta
    from sqlalchemy.future import select
    
    query = select(EmployeeTenant).filter(EmployeeTenant.tenant_id == tenant_id)
    result = db_session.execute(query)
    employees = result.scalars().all()

    return employees

def convert_and_process_employees(db_session: Session, tenant_id: str):
    """
    Obtiene los empleados y convierte payrollNumberBoss_id a string.
    """
    employees = get_employees(db_session, tenant_id)
    for employee in employees:
        payroll_id_str = convert_payroll_id_to_string(employee)
        print(f"Employee {employee.id} payrollNumberBoss_id: {payroll_id_str}")
