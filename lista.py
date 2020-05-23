import datetime
import csv
class Contacto :
    def __init__( self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTO):
        self.NICKNAME = ("BautistaM", "AcutisC", "AlbertoG", "LuisAlf", "OswaldoD", "Alcaraz", "CarranzaF", "ReyD", "Cupertino")
        self.NOMBRE = ("Jonathan", "Carlos", "Alberto", "Luis", "Oswaldo", "Astrid", "Federico", "Pedro", "Cupertino")
        self.CORREO = ("adrian.bautista0022@gmail.com", "carlosacutis@gmail.com", "albertogerardo51@gmail.com", "luisalfred745@gmail.com", "davidoswaldo147@gmail.com", "alcaraz01astrid@gmail.com", "federicocarranzaj@gmail.com", "davidelrey154@gmail.com","josecupertinotorres@gmail.com")
        self.TELEFONO = ("8128597883", "8184533327", "8115389095", "8117252091", "8131786580", "8131149495", "8123271601", "8131050403", "8134199382")
        self.FECHANACIMIENTO = ("04/05/2002", "03/05/1991", "15/07/1999", "09/12/1989", "06/06/2006", "22/10/2004", "16/09/2001", "12/12/2002","17/09/1993")
        self.GASTO = ("790.00", "900.00","850.00","750.00","600.00","590.00","480.00","590.00","990.00")
print("hola")