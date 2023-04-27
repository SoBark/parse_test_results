import pandas as pd
from bs4  import BeautifulSoup
from html.parser import HTMLParser

ball = 2
input_test_table_file_name = "message.html"
input_group_list="group_M3132.xlsx"
output_test_group_result = f"result_{input_group_list}.xlsx"
#output_test_result = "table.xlsx"

f = open(input_test_table_file_name, "r", encoding="UTF-8")
text = f.read()
f.close()
soup = BeautifulSoup(text, features="lxml")

div_w_test = soup.find_all("div", {"class": "w-full overflow-auto"})

table_cw= pd.read_html(str(div_w_test))[0]
max_ball = len(table_cw.columns.drop(['Id', 'Фамилия', 'Имя', 'Группа', 'Завершён?', 'Балл', 'Файл', 'Работа',]))
table_cw["ball"] = table_cw['Балл']/max_ball * ball

#table_cw.to_excel(output_test_result)

table_group = pd.read_excel(input_group_list)

data = table_group.merge(table_cw, "left")
data.to_excel(output_test_group_result)
