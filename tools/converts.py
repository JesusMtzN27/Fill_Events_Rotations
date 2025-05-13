from sqlalchemy import types

class DynamicNumberType(types.TypeDecorator):
    impl = types.String  # Usamos String por defecto, puede ser cambiado dinámicamente

    def __init__(self, *args, **kwargs):
        super(DynamicNumberType, self).__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        # Si el valor es de tipo BIGINT (número entero), lo convertimos a String
        if isinstance(value, int):  # Si el valor es de tipo BIGINT
            return str(value)  # Convertirlo a string antes de guardarlo
        return value  # Si ya es string, no hacemos nada

    def process_result_value(self, value, dialect):
        # Si el valor es un string que representa un número, lo devolvemos tal cual
        return value  # No modificamos el valor si ya es un string
