from xlrd import open_workbook
import sample_data_vo
class ExcelReader(object):
    def read_company_info(self, wb=None, wb_path=None):
        if wb is None:
            if wb_path is None:
                raise
            wb = open_workbook(wb_path)
        sheet_name = wb.sheet_by_name('sample_info')
        number_of_rows = sheet_name.nrows
        number_of_columns = sheet_name.ncols
        excel_sheet_info_list = []
        for row in range(1, number_of_rows):
            excel_sheet_info = sample_data_vo.SampleDataVo()
            for col in range(number_of_columns):
                if (str(sheet_name.cell(row,col).value)) is not None and (str(sheet_name.cell(row,col).value).strip()) != '':
                    if col == 0:
                        excel_sheet_info.id_number = (sheet_name.cell(row,col).value)
                    elif col == 1:
                        excel_sheet_info.database_Category = (sheet_name.cell(row,col).value)
                    elif col == 2:
                        excel_sheet_info.business_name = (sheet_name.cell(row,col).value)
                    elif col == 3:
                        excel_sheet_info.add1 = (sheet_name.cell(row,col).value)
                    elif col == 4:
                        excel_sheet_info.add2 = (sheet_name.cell(row,col).value)
                    elif col == 5:
                        excel_sheet_info.locality = (sheet_name.cell(row,col).value)
                    elif col == 6:
                        excel_sheet_info.town = (sheet_name.cell(row, col).value)
                    elif col == 7:
                        excel_sheet_info.county = (sheet_name.cell(row, col).value)
                    elif col == 8:
                        excel_sheet_info.postcode = (sheet_name.cell(row, col).value)
                    elif col == 9:
                        excel_sheet_info.Area = (sheet_name.cell(row, col).value)
                    elif col == 10:
                        excel_sheet_info.postcodearea = (sheet_name.cell(row, col).value)
                    elif col == 11:
                        excel_sheet_info.postcodesubarea = (sheet_name.cell(row, col).value)
                    elif col == 12:
                        excel_sheet_info.LineOfBusiness = (sheet_name.cell(row, col).value)
                    elif col == 13:
                        excel_sheet_info.sicnumeric = (sheet_name.cell(row, col).value)
                    elif col == 14:
                        excel_sheet_info.SIC_Description = (sheet_name.cell(row, col).value)
                    elif col == 15:
                        excel_sheet_info.telephone = (sheet_name.cell(row, col).value)
                    elif col == 16:
                        excel_sheet_info.tps = (sheet_name.cell(row, col).value)
                    elif col == 17:
                        excel_sheet_info.fax = (sheet_name.cell(row, col).value)
                    elif col == 18:
                        excel_sheet_info.fps = (sheet_name.cell(row, col).value)
                    elif col == 19:
                        excel_sheet_info.employeesnumeric = (sheet_name.cell(row, col).value)
                    elif col == 20:
                        excel_sheet_info.premises_type = (sheet_name.cell(row, col).value)
                    elif col == 21:
                        excel_sheet_info.title1 = (sheet_name.cell(row, col).value)
                    elif col == 22:
                        excel_sheet_info.fname1 = (sheet_name.cell(row, col).value)
                    elif col == 23:
                        excel_sheet_info.sname1 = (sheet_name.cell(row, col).value)
                    elif col == 24:
                        excel_sheet_info.position1 = (sheet_name.cell(row, col).value)
                    elif col == 25:
                        excel_sheet_info.email = (sheet_name.cell(row, col).value)
                    elif col == 26:
                        excel_sheet_info.Email_Address = (sheet_name.cell(row, col).value)
            excel_sheet_info_list.append(excel_sheet_info)

        return excel_sheet_info_list
