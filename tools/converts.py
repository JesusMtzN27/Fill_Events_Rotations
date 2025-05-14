from sqlalchemy import types
from sqlalchemy.dialects.postgresql import BIGINT

class DynamicSupervisorIDType(types.TypeDecorator):
    impl = types.String  # Usamos String por defecto, se puede cambiar dinámicamente.

    def __init__(self, *args, **kwargs):
        super(DynamicSupervisorIDType, self).__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):  # Si el valor es un número entero (BIGINT)
            return str(value)  # Lo convertimos a string
        return value  # Si ya es un string, lo dejamos igual

    def process_result_value(self, value, dialect):
        if isinstance(value, str) and value.isdigit():  # Si el valor es un string que representa un número
            return str(value)  # Lo devolvemos como string
        return value  # Si ya es string, lo dejamos igual
