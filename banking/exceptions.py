class BankingError(Exception):
    """Base class for banking errors"""
    pass


class InsufficientFundsError(BankingError):
    """Raised when balance is too low"""
    pass


class InvalidAmountError(BankingError):
    """Raised when amount is zero or negative"""
    pass


class MinimumBalanceError(BankingError):
    """Raised when minimum balance is violated"""
    pass