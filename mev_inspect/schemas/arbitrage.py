from typing import List

from pydantic import BaseModel

from .swaps import Swap


class Arbitrage(BaseModel):
    swaps: List[Swap]
    account_address: str
    profit_token_address: str
    start_amount: int
    end_amount: int
    profit_amount: int
