day1 = ["Alice@example.com", "bob@example.com", "ALICE@example.COM", "carol@example.com"]
day2 = ["bob@example.com", "dave@example.com", "Erin@example.com", "frank@example.com"]
day3 = ["carol@example.com", "GEORGE@example.com", "Hank@example.com", "alice@example.com"]
def clean_list(email_list):
    return set(email.lower() for email in email_list)
day1_clean = clean_list(day1)
day2_clean = clean_list(day2)
day3_clean = clean_list(day3)

all_attendees = day1_clean | day2_clean | day3_clean
total_unique = len(all_attendees)

attended_all_three = day1_clean & day2_clean & day3_clean

attended_one_day = (
    (day1_clean - day2_clean - day3_clean) |
    (day2_clean - day1_clean - day3_clean) |
    (day3_clean - day1_clean - day2_clean)
)

day1_day2_overlap = day1_clean & day2_clean
day2_day3_overlap = day2_clean & day3_clean
day1_day3_overlap = day1_clean & day3_clean

def print_report():
    print("Final Report:")
    print(f"1. Cleaned day1 list ({len(day1_clean)}): {sorted(day1_clean)}")
    print(f"1. Cleaned day2 list ({len(day2_clean)}): {sorted(day2_clean)}")
    print(f"1. Cleaned day3 list ({len(day3_clean)}): {sorted(day3_clean)}")
    print()
    print(f"2. Total unique attendees across all days: {total_unique}")
    print()
    print(f"3. Attendees who attended all three days ({len(attended_all_three)}): {sorted(attended_all_three)}")
    print()
    print(f"4. Attendees who attended exactly one day ({len(attended_one_day)}): {sorted(attended_one_day)}")
    print()
    print("5. Pairwise overlap counts and attendees:")
    print(f"   Day1 & Day2 ({len(day1_day2_overlap)}): {sorted(day1_day2_overlap)}")
    print(f"   Day2 & Day3 ({len(day2_day3_overlap)}): {sorted(day2_day3_overlap)}")
    print(f"   Day1 & Day3 ({len(day1_day3_overlap)}): {sorted(day1_day3_overlap)}")

print_report()
