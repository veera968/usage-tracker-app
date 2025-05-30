import datetime
import json
import os

DATA_FILE = "usage_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def track_usage(app_name):
    data = load_data()
    today = datetime.date.today().isoformat()
    if today not in data:
        data[today] = {}
    if app_name not in data[today]:
        data[today][app_name] = 0
    data[today][app_name] += 1
    save_data(data)
    print(f"Tracked usage for {app_name} on {today}.")

def show_report():
    data = load_data()
    for day, apps in data.items():
        print(f"Date: {day}")
        for app, count in apps.items():
            print(f"  {app}: {count} times")
        print()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple Usage Tracker App")
    parser.add_argument("--track", metavar="APP", help="Track usage of an app")
    parser.add_argument("--report", action="store_true", help="Show usage report")
    args = parser.parse_args()

    if args.track:
        track_usage(args.track)
    elif args.report:
        show_report()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()