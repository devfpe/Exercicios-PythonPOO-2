class ContaBancaria:
    def __init__(self, numero_da_conta: int, nome_do_titular: str, saldo: float):
        self._numero_da_conta: int = numero_da_conta
        self._nome_do_titular: str = nome_do_titular
        self._saldo: float = saldo

    def __str__(self) -> str:
        return f'[>> Numero da conta: {self._numero_da_conta} | Nome do titular: {self._nome_do_titular} | Saldo: {self._saldo} <<]'

    def deposito(self, valor_de_deposito: float):
        self._saldo += valor_de_deposito
        print(f'Saldo disponível pós-deposito: [>> {self._saldo} <<]')

    def saque(self, valor_de_saque: float):
        self._saldo -= valor_de_saque
        print(f'Saldo disponível pós-saque: [>> {self._saldo} <<]')

    def exibir_saldo(self) -> str:
        print(f'Saldo disponível na conta: [>> {self._saldo} <<]')