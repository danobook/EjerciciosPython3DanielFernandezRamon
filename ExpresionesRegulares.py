from FuncionEmail import ValidarEmail
from FuncionTelefono import ValidaTelefono
from FuncionRFC import ValidarRFC
from FuncionCurp import ValidarCurp
# Formatos validos usuario@padts.mx // usuario@padts.com.mx // usuario@python.padts.mx
ValidarEmail()
# Formatos validos 3312345678 // (33)12345678 // (331)1235678 // 33 1234 5678 // 33-1234-5678 // (331) 123-5678 // (331)-123-5678
ValidaTelefono()
# Formatos validos [Letra][Letra][Letra][Letra][Entero][Entero][Entero][Entero][Entero][Entero]
# FERD860728
ValidarRFC()
# Formatos validos [Letra][Letra][Letra][Letra][Entero][Entero][Entero][Entero][Entero][Entero][Letra][Letra][Letra][Consoante][Consonante][Consonante][Entero][Entero]
# FERD860728HMCNRM45
ValidarCurp()