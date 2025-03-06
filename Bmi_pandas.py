import pandas as pd

column = ["Sandi", "Maureen", "Laureen", "Zan", "Matej"]
titled_columns = {"Imena": column,
                 "Višina": [1.97,1.65,1.65,1.80,1.82],
                 "Teža": [100,60,59,85,80]


                 }

data = pd.DataFrame(titled_columns)
izbira= data["Višina"][1]
select_row = data.iloc[1]["Teža"]

bmi = []

for i in range(len(data)):
    bmi_score = data["Teža"][i]/(data["Višina"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

print(data)

