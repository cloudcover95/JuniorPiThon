import time
import logging

class PiTokenEcosystem:
    """Manages the Pi-based economy within the JuniorPiThon application."""
    def __init__(self):
        self.blueprint_registry = {}

    def authorize_compute_gas(self, user_id: str, compute_cycles: int) -> bool:
        """Charges a micro-Pi fee for continuous edge execution."""
        pi_cost = compute_cycles * 0.0001
        logging.info(f"Charging {user_id} {pi_cost} Pi for edge compute allocation.")
        return True # Mocked Pi SDK A2A payment verification

    def publish_blueprint(self, user_id: str, script_name: str, code: str, price_pi: float):
        """Registers a user script to the decentralized marketplace."""
        b_id = f"BP_{int(time.time())}"
        self.blueprint_registry[b_id] = {"author": user_id, "name": script_name, "price": price_pi}
        logging.info(f"Blueprint {script_name} published at {price_pi} Pi.")
        return b_id
