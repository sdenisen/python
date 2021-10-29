import re

file_path = []
import pandas as pd
from collections import defaultdict

winnodes = [
    r".*qawinnode184.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
    r".*qawinnode185.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
    r".*qawinnode186.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
    r".*qawinnode187.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
    r".*qawinnode188.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
    r".*qawinnode189.tf.five9lab.com.*action: (?!func_wrapper2)(\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)",
]

row_index = 0
row_index_average = 0

for winnode in winnodes:
    win_node_name = winnode.split(".*")[1]
    writer = pd.ExcelWriter(f"statistics_{win_node_name}.xlsx", engine="xlsxwriter")
    workbook = writer.book
    worksheet = workbook.add_worksheet("Result")
    worksheet_average = workbook.add_worksheet("Average Time")
    writer.sheets["Result"] = worksheet
    writer.sheets["Average Time"] = worksheet_average

    with open("log_211028_025907-23109.txt", "r") as f:

        found_new_test_script = False
        s = defaultdict(list)
        script_name = ""
        while True:
            l = f.readline()
            if not l:
                break

            match2 = re.search(r"stdout: Test is finished: Status:", l)
            match_script_name = re.search(r"stdout: Test is started: (\w+)\.py", l)

            if match_script_name:
                found_new_test_script = True
                script_name = match_script_name.groups()[0]
                action_lst = []
                duration_lst = []
                start_time_lst = []
                stop_time_lst = []
                transaction_count = 0
                s = defaultdict(list)

            if found_new_test_script:
                match = re.search(winnode, l)
                if match:
                    print(match.groups())
                    ll_tuple = match.groups()
                    action_lst.append(ll_tuple[0])
                    duration_lst.append(round(float(ll_tuple[1]), 3))
                    start_time_lst.append(ll_tuple[2])
                    stop_time_lst.append(ll_tuple[3])
                    s[ll_tuple[0]].append(round(float(ll_tuple[1]), 3))
                    transaction_count +=1

            if match2:
                found_new_test_script = False
                data = {
                    "Agent Action": action_lst,
                    "Begin time(H:M:S)": start_time_lst,
                    "End time(H:M:S)": stop_time_lst,
                    "Duration (in seconds)": duration_lst
                }
                rows = len(action_lst)
                df = pd.DataFrame(data)
                print(data)
                print("save to file")
                worksheet.write_string(row_index, 0, f"script_name:")
                worksheet.write_string(row_index, 1, f"{script_name}")
                row_index += 1
                df.to_excel(writer, sheet_name="Result", startrow=row_index, startcol=1)
                row_index += rows
                row_index += 5

                worksheet_average.write_string(row_index_average, 0, f"script_name:")
                worksheet_average.write_string(row_index_average, 1, f"{script_name}")
                row_index_average += 1

                worksheet_average.write_string(row_index_average, 0, f"transaction count:")
                worksheet_average.write_string(row_index_average, 1, f"{transaction_count}")
                row_index_average += 1
                worksheet_average.write_string(row_index_average, 0, "Average action time:")
                row_index_average += 1
                data_max = {
                    "Agent Action": s.keys(),
                    "Max action time (in seconds)": [max(s[key]) for key in s.keys()]
                }
                df_max = pd.DataFrame(data_max)
                df_max.to_excel(writer, sheet_name="Average Time", startrow=row_index_average, startcol=1)
                row_index_average += len(s.keys())
                row_index_average += 1

                data_min = {
                    "Agent Action": s.keys(),
                    "Min action time (in seconds)": [min(s[key]) for key in s.keys()]
                }
                df_min = pd.DataFrame(data_max)
                df_min.to_excel(writer, sheet_name="Average Time", startrow=row_index_average, startcol=1)
                row_index_average += len(s.keys())
                row_index_average += 1

                data_average = {
                    "Agent Action": s.keys(),
                    "Average time (in seconds)": [round(sum(s[key]) / float(len(s[key])), 3) for key in s.keys()]
                }
                df_average = pd.DataFrame(data_average)
                df_average.to_excel(writer, sheet_name="Average Time", startrow=row_index_average, startcol=1)
                row_index_average += len(s.keys())
                row_index_average += 1

    writer.save()