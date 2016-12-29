from excel_reader.excel_file_helper import  excel_sheet_helper
def save_excel_sheet_info():
    wb_path = 'd:\\excel_sheets\\sample_info.xlsx'
    excel_sheet_helper.ExcelSheetHelper().save_info_from_xlrd(wb_path)
save_excel_sheet_info()

def get_excel_sheet_info_list():
    excel_sheet_helper.ExcelSheetHelper().get_excel_sheet_info_list(1, 15)
get_excel_sheet_info_list()
