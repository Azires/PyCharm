import pandas as pd
from datetime import datetime

df = pd.read_excel("Obiski EQ lokacij 2025.xlsx")

payslip_month = datetime(2025, 1, 1)

df['Datum'] = pd.to_datetime(df['Datum'], format='%d. %m. %Y')

filtered_df = df[(df['Datum'].dt.month == payslip_month.month) &
                 (df['Datum'].dt.year == payslip_month.year) &
                 (df['Status'] == 'realizirano')]


def reverse_normalize_name(name):
    return name.lower()


filtered_df.loc[:, 'Voznik'] = filtered_df['Voznik'].apply(reverse_normalize_name)


worklogs = []

for user, row in filtered_df.iterrows():
    worklog = {
        "date": row["Datum"].strftime('%m-%Y'),
        "primary/secondary": row["Relacija"],
        "travel_distance": row.get("Travel_distance", "km"),
        "driver": row["Voznik"]
    }
    worklogs.append(worklog)


worklog_df = pd.DataFrame(worklogs)

worklog_df.to_excel('worklog.xlsx', index=False)

print("Worklog created successfully!")
