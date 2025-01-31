import os

def extract_logs(log_file, target_date, output_dir="tech-campus-recruitment-2025\output"):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.startswith(target_date):
                    outfile.write(line)

        print(f"Logs for {target_date} saved to {output_file}")

    except FileNotFoundError:
        print("Error: Log file not found. Check Log file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(script_dir, "logs_2024.log")
    target_date = input("Enter the date (YYYY-MM-DD) to extract logs: ").strip()

    extract_logs(log_file, target_date)
