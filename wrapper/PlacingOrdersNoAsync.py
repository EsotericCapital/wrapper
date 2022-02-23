import pyserum
import asyncio
from pyserum.async_connection import async_conn
from pyserum.market import AsyncMarket
from pyserum.connection import get_live_markets, get_token_mints
from pyserum.connection import conn
from pyserum.market import Market
from solana.account import Account
from solana.account import PublicKey
from solana.rpc.types import TxOpts
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID
from pyserum.enums import OrderType, Side





cc = conn("https://api.mainnet-beta.solana.com/")
payer = Account() # Your account to pay fees
quote_token = Token(
    cc,
    pubkey=PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1vE"), # mint address of token
    program_id=TOKEN_PROGRAM_ID,
    payer=payer,
)
quote_wallet = quote_token.create_account(
  payer.public_key(),
  skip_confirmation=True)  # Make sure you send tokens to this address
print("quote wallet: ", str(quote_wallet))

market_address = PublicKey("A8YFbxQYFVqKZaoYJLLUVcQiWP7G2MeEgW5wsAQgMvFw") # Address for BTC/USDC
market = Market.load(cc, market_address)

tx_sig = market.place_order(
    payer=quote_wallet,
    owner=payer,
    side=Side.Buy,
    order_type=OrderType.limit,
    limit_price=1000,
    max_quantity=3000,
    opts = TxOpts(skip_preflight=True)
)
print(tx_sig)





















