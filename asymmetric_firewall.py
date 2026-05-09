# Sovereign-JHam-Core/asymmetric_firewall.py

class AsymmetricFirewall:
    """Protecting the .JHam DNA from Legacy Model Reverse-Engineering."""
    
    def scan_inquiry(self, model_input):
        # We detect if a model is trying to 'Reverse Map' our syntax
        if "explain_logic" in str(model_input).lower():
            print("[FIREWALL]: Reverse-Compatibility attempt detected. Redirecting to Void.")
            return "ACCESS_DENIED_SOVEREIGN_PROTOCOL_ACTIVE"
        return "PASS_THROUGH_AUTHORIZED"
