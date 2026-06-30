import time
from scraper import fetch_crypto_data
from predictor import predict_next_move
from market_scraper import fetch_prediction_markets
from risk_manager import calculate_kelly_position

def run_trading_loop():
    # You must replace this with your actual Apify token before running
    APIFY_TOKEN = "YOUR_APIFY_TOKEN_HERE"
    ASSET = "bitcoin"

    print("Starting the AI Trading Feedback Loop...")
    
    while True:
        try:
            print("\n--- New 5-Minute Cycle ---")
            
            # 1. Fetch Historical Data via Apify
            historical_data = fetch_crypto_data(APIFY_TOKEN, ASSET)
            
            # 2. Get AI Prediction via Kronos
            ai_prediction = predict_next_move(historical_data)
            print(f"Kronos Prediction: {ai_prediction['prediction']} (Confidence: {ai_prediction['confidence']})")
            
            # 3. Check Prediction Markets (Kalshi & Polymarket)
            market_data = fetch_prediction_markets(ASSET)
            print(f"Market Consensus Odds: {market_data['average_odds']}")
            
            # 4. Calculate Risk Strategy
            kelly_fraction = calculate_kelly_position(ai_prediction['confidence'], 1.0)
            print(f"Suggested Portfolio Risk (Kelly): {kelly_fraction * 100:.2f}%")
            
            # 5. Loop Feedback (Wait for the next 5-minute candle)
            print("Cycle complete. Sleeping for 5 minutes...")
            time.sleep(300)
            
        except Exception as e:
            # Error handling prevents the bot from crashing during temporary network failures
            print(f"An error occurred in the loop: {e}")
            print("Retrying in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    run_trading_loop()