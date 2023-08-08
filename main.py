"""
Summary


"""

from mt5_server import MetaTrader5


mt5 = MetaTrader5(host='192.168.31.251', port=18812)
mt5.initialize()
info = mt5.account_info()

print(info)
