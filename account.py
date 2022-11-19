class Account:
    def __init__(self, name: str):
        '''
        Sets the account name and balance
        :param name: Account name
        '''
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self, amount: float) -> bool:
        '''
        Deposit money into account. Only deposits if a positive number
        :param amount: Amount deposited into account
        :return: If deposit went through or not
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True


    def withdraw(self, amount: float) -> bool:
        '''
        Withdraw from account. Cannot withdraw more than total ammount and <=0.
        :param amount: Amount Withdrawn
        :return: IF the withdraw went through
        '''
        if self.__account_balance < amount:
            return False
        elif amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Shows you your account balance
        :return: the account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Shows you the name on the account.
        :return: account name
        '''
        return self.__account_name


