def calculate_kelly_position(win_probability, odds_multiplier):
    """
    Calculates position sizing using the Kelly formula.
    win_probability: Kronos confidence (e.g., 0.55 for 55%)
    odds_multiplier: Decimal payout odds from Kalshi/Polymarket
    """
    q = 1 - win_probability
    
    # Kelly Formula: f* = p - (q / b)
    kelly_fraction = win_probability - (q / odds_multiplier)
    
    # Return 0 if the formula suggests a negative bet (bad odds)
    return max(0.0, kelly_fraction)