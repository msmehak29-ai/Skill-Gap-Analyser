import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from colorama import Fore, Style, init

# Initialize colorama for cross-platform terminal colors
init(autoreset=True)

# --- 2026 BENCHMARK DATA ---
MARKET_ROLES = {
    "1": {"name": "AI/ML Engineer", "skills": [1.0, 0.9, 0.8, 0.6, 0.9]},
    "2": {"name": "Full-Stack Dev", "skills": [0.6, 0.4, 1.0, 0.8, 0.9]},
    "3": {"name": "Cloud Architect", "skills": [0.5, 0.8, 1.0, 0.9, 0.7]}
}
SKILL_LABELS = ["Agentic AI", "MLOps", "Cloud Native", "Cybersecurity", "DSA"]

def display_market_trends():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}--- 2026 MARKET TRENDS (STATISTICAL SUMMARY) ---")
    data = [
        ["Agentic AI", "+156%", "53% Deficit", "₹25L+"],
        ["Cybersecurity", "+35%", "30% Deficit", "₹18L+"],
        ["Cloud Native", "+28%", "55% Deficit", "₹16L+"]
    ]
    print(f"{'Specialization':<20} | {'Growth':<8} | {'Shortage':<12} | {'Avg Salary'}")
    print("-" * 60)
    for row in data:
        print(f"{row[0]:<20} | {Fore.GREEN}{row[1]:<8}{Fore.RESET} | {row[2]:<12} | {row[3]}")

def run_analysis():
    print(f"{Fore.YELLOW}{Style.BRIGHT}Welcome to the 2026 CS Skill Gap CLI Analyzer")
    display_market_trends()

    print(f"\n{Fore.MAGENTA}Select Target Role:")
    for k, v in MARKET_ROLES.items():
        print(f"{k}. {v['name']}")
    
    choice = input("\nEnter choice (1-3): ")
    if choice not in MARKET_ROLES:
        print("Invalid choice. Exiting.")
        return

    target = MARKET_ROLES[choice]
    print(f"\n{Fore.YELLOW}Rate your proficiency (0.0 to 1.0) for the following:")
    
    user_ratings = []
    for skill in SKILL_LABELS:
        val = float(input(f" - {skill}: "))
        user_ratings.append(val)

    # Calculation Logic
    user_vec = np.array(user_ratings).reshape(1, -1)
    target_vec = np.array(target['skills']).reshape(1, -1)
    score = cosine_similarity(user_vec, target_vec)[0][0]

    # Results Output
    print(f"\n{Fore.WHITE}{Style.BRIGHT}================ RESULT ================")
    status_color = Fore.GREEN if score > 0.7 else Fore.RED
    print(f"Target Role: {target['name']}")
    print(f"Market Alignment Score: {status_color}{score:.2%}")
    
    print(f"\n{Fore.YELLOW}CRITICAL GAPS IDENTIFIED:")
    for i, skill in enumerate(SKILL_LABELS):
        gap = target['skills'][i] - user_ratings[i]
        if gap > 0.2:
            print(f" [!] {skill}: {Fore.RED}-{gap:.1%} deficit{Fore.RESET}")

    print(f"{Fore.WHITE}{Style.BRIGHT}========================================\n")

if __name__ == "__main__":
    run_analysis()
