import pandas as pd
import requests
import tabula

from Spider.geocoder import extract_lat_long_via_address


def create_address_table(url):
    final_table = []
    pg_num = 0
    while pg_num <= 1:
        website = f"{url}?pagenum={pg_num}"
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0'}
        result = requests.get(website, headers=user_agent)
        table = pd.read_html(result.text)
        final_table.append(table[0])
        pg_num += 1
    else:
        final_table = pd.concat(final_table)
        df = pd.DataFrame(final_table)
        add_list = []
        for index, row in df.iterrows():
            address = (row["Name"]), (row["Address"]), extract_lat_long_via_address(row["Name"], row["Address"])
            add_list.append(address)
        print(add_list)
        df = pd.DataFrame(add_list)
        writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='addresses', index=False)
        writer.save()


def address_table(pdf):
    from tabula import read_pdf
    from tabulate import tabulate
    table = tabula.read_pdf(pdf, pages=1)
    print(table[0].df)


create_address_table("https://savc.org.za/wp-content/uploads/2023/03/Active-Facilities-March-2023.pdf")