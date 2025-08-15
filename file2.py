import pandas as pd
from fpdf import FPDF
from datetime import datetime

# read the data
data=pd.read_csv("sales_data.csv")

# data analyze
summary=data.groupby("Region")["Sales"] .agg(["sum","mean","max","min"]).reset_index()

# df report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial","B",12)
        self.cell(0,10,"Sales Report",ln=1,align="C")
        self.set_font("Arial","",10)
        self.cell(0,10,f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",ln=1,align="C")
        self.ln (10)

    def add_table(self,dataframe):
        self.set_font("Arial","B",12)
        col_widths=[40,35,30,25,20]
        headers=["Region","Total Sales","Average Sales","Max Sales","Min Sales"]
        for i,header in enumerate(headers):
            self.cell(col_widths[i],10,header,border=1,align="C")
            self.ln()

            self.set_font("Arial","",11)
            for index,row in dataframe.iterrows():
                self.cell(col_widths[0],10,str(row["Region"]),border=1)
                self.cell(col_widths[1],10,f"${row['sum']:,.2f}",border=1,align='R')
                self.cell(col_widths[2],10,f"${row['mean']:.2f}",border=1,align='R')
                self.cell(col_widths[3],10,f"${row['max']:.2f}",border=1,align='R')
                self.cell(col_widths[4],10,f"${row['min']:.2f}",border=1,align='R')
                self.ln()

# pdf generate
pdf=PDFReport()
pdf.add_page()
pdf.add_table(summary)
pdf.output("file2.pdf")

print("PDF report generated as 'file2'")
