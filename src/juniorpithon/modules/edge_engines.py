import random

class JuniorHomeIoT:
    """Edge-native IoT bridge for 48V LiFePO4 / Solar telemetry."""
    @staticmethod
    def get_telemetry() -> dict:
        return {
            "battery_soc": round(random.uniform(84.0, 86.0), 1),
            "solar_watts": round(random.uniform(1150.0, 1250.0), 1),
            "load_watts": round(random.uniform(300.0, 350.0), 1),
            "system_health": "OPTIMAL"
        }

class MarketTracker:
    """Lightweight OHLCV tracker for Stocks and Web3."""
    def __init__(self):
        self.prices = {"PI-USD": 42.50, "BTC-USD": 64500.00, "TSLA": 175.20}
        
    def get_market_state(self) -> dict:
        for ticker in self.prices:
            drift = random.normalvariate(0, self.prices[ticker] * 0.002)
            self.prices[ticker] += drift
        return {k: round(v, 2) for k, v in self.prices.items()}
