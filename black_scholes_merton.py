import math
import scipy

S = 95  # Current Stock Price (also called Spot Price)
K = 90  # Option Strike price
sigma = 0.22  # Standard Deviation per year in percent (Volatility)
r = 0.02  # The risk-free interest rate
t = 90  # Time in days until expiration

def black_scholes_model_call(S, sigma, r, t, K):
    t = t / 365
    d1 = (math.log(S / K) + ((r + ((sigma ** 2) / 2)) * t)) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    c = (S * scipy.stats.norm.cdf(d1) - K * math.e ** (-r * t) * scipy.stats.norm.cdf(d2)).round(2)
    return c


def black_scholes_model_put(S, sigma, r, t, K):
    t = t / 365
    d1 = (math.log(S / K) + ((r + ((sigma ** 2) / 2)) * t)) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    p = (K * math.e ** (-r * t) * scipy.stats.norm.cdf(-d2) - S * scipy.stats.norm.cdf(-d1)).round(2)
    return p


print(f"Price of the Call Option: ${black_scholes_model_call(S, sigma, r, t, K)}")
print(f"Price of the Put Option: ${black_scholes_model_put(S, sigma, r, t, K)}")
