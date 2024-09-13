import re
import os
import glob
import time
import logging
import pandas as pd
from datetime import datetime
from utils.dateValidations import is_valid_date
import PyPDF2

from utils.webDriver import webDriver

def pdfProcessing(driver, permit): #0


    try:
        print(f"Downloading PDF file for permit number {permit} ....")
        
        driver = pdfDownload(driver,permit=permit)
        time.sleep(2.6)
        pdf_df = scrapData(permit=permit)
        try:
            if pdf_df['Purpose'].value_counts()['Sell'] > 0:
                count_Buy = pdf_df['Purpose'].value_counts()['Sell']
            else:
                count_Rent = 0
        except:
            count_Buy = 0
        try:
            if pdf_df['Purpose'].value_counts()['Rent'] > 0:
                count_Rent = pdf_df['Purpose'].value_counts()['Rent']
            else:
                count_Rent = 0
        except:
            count_Rent = 0

        print("loading file ....")
        print(f"Listing Counts is: \ncount_Buy -> {count_Buy} \ncount_Rent -> {count_Rent}\n..............................................")

        agencies = []
        expire_dates = []

        for i in range(3):
            if i < int(count_Buy) + int(count_Rent):
                agencies.append(pdf_df['Trade_Name'][i])
                expire_dates.append(pdf_df['End_Date'][i])
            else:
                agencies.append("None")
                expire_dates.append("None")

        agency1 = agencies[0]
        agency2 = agencies[1]
        agency3 = agencies[2]
        expire_date1 = expire_dates[0]
        expire_date2 = expire_dates[1]
        expire_date3 = expire_dates[2]

        return driver,agency1,agency2,agency3,expire_date1,expire_date2,expire_date3
    except Exception as e:
        print("Error while compiling pdfProcessing function",e)




def pdfReads(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()

    return text
    


def pdfDownload(driver,permit=''): #0
    permit = permit
    link = f"https://trakheesi.dubailand.gov.ae/General/ValidatePrintReport.aspx?reportType=19&transactionNumber={permit}"
    driver.get(link)
    time.sleep(2)
    try:
        pdfPreload(new_filename=permit)
    except:
        print("The Property Listing PDF File might not Found")
    return driver
    

def pdfPreload(filename='./db/Files/downloads', new_filename=''): #00
    time.sleep(2.1)
    files2 = glob.glob(filename + '/*')
    max_file = max(files2, key=os.path.getctime)
    filename = max_file.split("/")[-1].split(".")[0]
    try:
        # if the file already downloaded add new file or replace
        new_path = max_file.replace(filename, new_filename)
        os.rename(max_file, new_path)
    except FileNotFoundError as e:
        logging.ERROR(e)
        print("File not found")
        


def scrapData(permit):#1


    pdf_text = pdfReads(f'./db/Files/downloads/{permit}.pdf')

    pdf_text = (pdf_text.strip().replace('\xa0', ' ').split('\n'))
    start_number = pdf_text.index('Company/ Institution that marketing same project or unit.')
    end_number = pdf_text.index(pdf_text[-8])
    table = pdf_text[start_number+1:end_number]
    columns = ['End Date', 'Start Date', 'Purpose','Transaction','License','Trade Name']
    lines  = table[4:]

    num_columns = 6

    dataT = []
    try:
        for i in range(0, len(lines), num_columns):
            dataT.append(lines[i:i+num_columns])

        df = pd.DataFrame(dataT,columns=columns)

        history = []
        for line in lines[::3]:
            line_clean = line.replace('ﺑﻴﻊ','').replace('ﺍﻳﺠﺎﺭ','').split(' ')
            if is_valid_date(line_clean[0]):
                history.append(line_clean)
                lines.remove(line)

    except Exception as e:
        print("Error define data",e)


    try:
        Purpose = []
        for id,ele in enumerate(lines):
            if ele[:4] == 'Rent' or ele[:4] == 'Sell':
                Purpose.append(ele[:4])
                lines[id] = ele.replace(ele[:5], '')

            
        number =''
        for line in lines:
            match = re.search(r'(\b\d+)\s+[A-Z]', line)
            if match:
                number = match.group(1)


        pattern = re.compile(r'\d{3,}')
        T_L_number = []
        for line in lines:
            data = pattern.findall(line.replace(number,''))
            if data:
                T_L_number.append( pattern.findall(line.replace(number,'')))
                lines.remove(line)



        if "(B" in lines[-1]:
            lines[-2] += lines[-1]
            # Remove the current item containing "(BRANCH)"
            lines.pop(-1)


        Trade_Name = []
        for line in lines:
            if '/' in line:
                line = line.split('/')[0]
                Trade_Name.append(line)
    except Exception as e:
        print("Error while check data",e)

    try:
        merged_data = []
        for name, hist, purpose, numbers in zip(Trade_Name, history, Purpose, T_L_number):

            End_Date = datetime.strptime( hist[0], '%d/%m/%Y')
                    # if (datetime.now() - date) < timedelta(days=3 * 365):
            if  datetime.now() < End_Date:
                End_Date = End_Date.strftime('%d/%m/%Y')    
                # print(hist[0])
                merged_entry = {
                    'Trade_Name': name,
                    'Start_Date': hist[1],
                    'End_Date': End_Date,
                    'Purpose': purpose,
                    'Transaction': numbers[0],
                    'License':numbers[1]
                }
                merged_data.append(merged_entry)

    except:
        print("Error while merging data",e)

    try:
        df = pd.DataFrame(merged_data)
        df = df.sort_values(by='End_Date',ascending=False)
        df.to_csv(f'./db/Files/Loaded_PDF/{permit}.csv',index=None)
        print(f"file data loaded as df and saved : db/Files/Loaded_PDF/{permit}.csv")
    except Exception as e:
        print("Error while Save data",e)

    return df




if __name__ == "__main__":
    try:
        driver = webDriver()

        driver,agency1,agency2,agency3,expire_date1,expire_date2,expire_date3 = pdfProcessing(driver,permit='7117842574')
        print('pdfProcessing done')
        driver().close()

    except Exception as e:
        print("..........................................................................................")
