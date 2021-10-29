import re
from collections import defaultdict
import pandas as pd


path_to_log_files = ['test_script_logs/log_file_rest_api_login_logout_test.txt',
                     'test_script_logs/log_file_rest_api_set_state_test.txt',
                     'test_script_logs/log_file_rest_api_add_remove_campaigns_skills.txt',
                     'test_script_logs/log_file_rest_api_modify_skills.txt',
                     'test_script_logs/log_file_rest_api_add_remove_user_group_skills.txt',]
for path in path_to_log_files:
    script_name = path.split("/")[1]
    with open(path, "r") as f:
        s = defaultdict(list)
        transaction_count = 0
        while True:
            l = f.readline()
            if not l:
                break

            pattern = r"action: (\w+); DURATION: ([0-9,.]*); START_TIME: ([0-9,:]*); STOP_TIME: ([0-9,:]*)"
            match = re.search(pattern, l)
            if match:
                ll_tuple = match.groups()
                transaction_count += 1
                _action = ll_tuple[0]
                _duration = round(float(ll_tuple[1]), 3)
                s[_action].append(_duration)

    print(transaction_count)
    data_average = {
        "Agent Action": s.keys(),
        "Average time (in seconds)": [ round(sum(s[key])/ float(len(s[key])), 3) for key in s.keys()]
    }
    df1 = pd.DataFrame(data_average)
    df1.name = "Average action time:"
    # df.to_excel(f'data_average_{script_name}.xlsx', index=False)

    data_max = {
        "Agent Action": s.keys(),
        "Max action time (in seconds)": [ max(s[key]) for key in s.keys()]
    }
    df2 = pd.DataFrame(data_max)
    df2.name = "Max action time"
    # df.to_excel(f'data_max_{script_name}.xlsx', index=False)

    data_min = {
        "Agent Action": s.keys(),
        "Max action time (in seconds)": [ min(s[key]) for key in s.keys()]
    }
    df3 = pd.DataFrame(data_min)
    df3.name = "Minimum action time"
    # df.to_excel(f'data_min_{script_name}.xlsx', index=False)

    print("save to file")
    writer = pd.ExcelWriter(f"statistics_{script_name}.xlsx", engine="xlsxwriter")
    workbook = writer.book
    worksheet = workbook.add_worksheet("Result")
    writer.sheets["Result"] = worksheet

    worksheet.write_string(0,0, f"transaction count:")
    worksheet.write_string(0,1, f"{transaction_count}")

    worksheet.write_string(1,0, df1.name)
    df1.to_excel(writer, sheet_name="Result", startrow=2, startcol=1)

    worksheet.write_string(df1.shape[0]+5, 0, df2.name)
    df2.to_excel(writer, sheet_name="Result", startrow=df1.shape[0]+6, startcol=1)

    worksheet.write_string(df1.shape[0]+6 + df2.shape[0]+5, 0, df2.name)
    df3.to_excel(writer, sheet_name="Result", startrow=df1.shape[0]+5 + df2.shape[0]+5, startcol=1)

    writer.save()

    print(data_average)
    print(data_max)
    print(data_min)
