from pathlib import Path
import subprocess
import os

rootdir = Path(os.path.dirname(os.path.realpath(__file__)))

file_list = [str(f) for f in rootdir.glob('*') if f.is_dir()]
filters = "grep -v package-lock | grep -v bak | grep -v test | grep -v .json | grep .js | "

def print_total_lines_added_for_author(author, start_date, end_date):
    total = 0

    for path in file_list:
        os.chdir(path)
        command = "git log --author=\"" + author + "\" --after=\"" + start_date + "\" --before=\"" + end_date + "\"" + r""" --pretty=tformat: --numstat | """ + filters +  r"""awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "%s", add, subs, loc }' -"""

        results = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

        total += int(results.stdout or 0)

    print(str(total) + " lines of code added between " + start_date + " and " + end_date + " by " + author)

print_total_lines_added_for_author("axs221\|hawn", "8/1/2017", "2/8/2018")
