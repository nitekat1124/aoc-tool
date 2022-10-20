import argparse, datetime, os
import urllib.request, urllib.parse


def main():
    year = datetime.date.today().year

    files = ["solutions/day_sample.py", "utils/puzzle_reader.py", "utils/solution_base.py", "utils/submission.py", "LICENSE", "README.md", "app.py"]
    remote_address = "https://raw.githubusercontent.com/nitekat1124/aoc-tool/files/template-files/"

    parser = argparse.ArgumentParser(description="Advent of Code Tool")
    parser.add_argument("-y", "--year", dest="year", required=False, default=year, metavar="year_number", type=int, help="the year of the AoC event")
    parser.add_argument("-t", "--target", dest="target", required=False, default=".", metavar="target_dir", type=str, help="target directory for the AoC files")
    parser.add_argument("-p", "--prefix", dest="prefix", required=False, default="advent-of-code", metavar="dir_prefix", type=str, help="prefix for the AoC files directory")
    args = parser.parse_args()

    if args.prefix in [None, ""]:
        args.prefix = "advent-of-code"

    path = os.path.realpath(os.path.join(os.getcwd(), args.target, args.prefix + "-" + str(args.year)))
    if os.path.exists(path):
        print("Directory already exists: " + path)
        return
    else:
        to_create = input(f"target: {path}\nwant to create directory and files? [y/N] ")
        if to_create.lower() == "y":
            os.makedirs(path)
            print("Created directory: " + path)

            for file in files:
                remote_file = remote_address + file
                with urllib.request.urlopen(remote_file) as response:
                    remote_content = response.read().decode("utf-8")

                local_file = os.path.join(path, file)
                local_file_dir = os.path.dirname(local_file)

                if not os.path.exists(local_file_dir):
                    os.makedirs(local_file_dir)
                    print("Created directory: " + local_file_dir)

                with open(local_file, "w+") as f:
                    f.write(remote_content)
                    print("Created file: " + local_file)

            print("Done!")


if __name__ == "__main__":
    main()
