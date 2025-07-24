import sys
import logging

sys.path.append("../")
import tossinvest_sock

#[*] trade:  {'code': 'US20220225003', 'dt': '2025-07-24T06:56:04Z', 'session': 'DAY', 'currency': 'USD', 'base': 1.01, 'close': 1.42, 'baseKrw': 1392.891, 'closeKrw': 1958.322, 'volume': 23, 'tradeType': 'BUY', 'changeType': 'UP', 'tradingStrength': 176.27, 'cumulativeVolume': 378269, 'cumulativeAmount': 506617, 'cumulativeAmountKrw': 698675504.7}

class SubscribeTest:
    def handle_tade(self, trade: tossinvest_sock.Trade): 
        print("[*] trade: ", trade)
        pass

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    st = SubscribeTest()
    worker = tossinvest_sock.connect_toss(st.handle_tade)
    worker.register_stock("US20220225003")
    