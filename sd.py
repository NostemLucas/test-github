class CuentaBancaria:
    
    def __init__(self,titular,numeroCuenta,saldo=0):
        self.titular = titular
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
    
    def mostrarInfo(self):
        print("==================================")
        print(f"numeroCuenta: {self.numeroCuenta}")
        print(f"titular: {self.titular}")
        print(f"saldo: ', {self.saldo}")
        print("==================================")

    def aumentarSaldo(self, monto):
        self.saldo += monto
    
    def disminuyeSaldo(self, monto):
        if self.saldo < monto:
            print('Saldo Insuficiente')
        else:
            self.saldo -= monto
    
#metodos

cuentas = []

def crearCuenta(titular,numeroCuenta,saldo):
    cuenta = CuentaBancaria(titular,numeroCuenta,saldo)
    cuentas.append(cuenta)
    print('Cuenta creada correctamente')
  

def mostrarCuentas():
    if not cuentas:
        print('NO HAY CUENTAS')
    else:
        for cuenta in cuentas:
            cuenta.mostrarInfo()   
  

def realizarDeposito(numeroCuenta, monto):
    cuenta = buscarCuenta(numeroCuenta)
    if cuenta:
        cuenta.aumentarSaldo(monto)
  
def retirarMonto(numeroCuenta, monto):
    cuenta = buscarCuenta(numeroCuenta)
    #if cuenta:
        #cuenta.disminuyeSaldo(monto)
  
def buscarCuenta(numeroCuenta):
    for cuenta in cuentas:
        if cuenta.numeroCuenta == numeroCuenta:
            return cuenta
    print('CUENTA NO ENCONTRADA')
    return None
   
#bucle
while True:
    print("""
    =============MENU=============
    1. CREAR CUENTA
    2. MOSTRAR CUENTAS
    3. DEPOSITAR DINERO
    4. RETIRAR DINERO
    5. SALIR
    """)
    valor = input('Seleccion Opcion ')
    if valor == "1":
        numeroCuenta = input('Ingrese el numero de cuenta: ')
        titular = input('Ingrese el nombre de titular: ')
        saldo = int(input('Ingrese el monto inicial: '))
        cuenta = crearCuenta(titular,numeroCuenta,saldo)
    elif valor == "2":
        mostrarCuentas()
    elif valor == "3":
        numeroCuenta = input('Ingrese el numero de cuenta: ')
        monto = int(input('Ingrese el monto: '))
        realizarDeposito(numeroCuenta,monto)
    elif valor == "4":
        retirarMonto()
    else:
        break

    
    