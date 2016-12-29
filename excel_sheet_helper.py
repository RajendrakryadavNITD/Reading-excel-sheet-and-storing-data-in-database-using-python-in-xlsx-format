import os
from flask import current_app
from excel_reader import excel_sheet_reader, sample_data_vo
from excel_reader.dal import connection_factory, transactionutils
from excel_reader.dao import dao_factory
from xlrd import open_workbook

class ExcelSheetHelper(object):
    def get_connection(self, existing_conn=None):
        is_new_connection = False
        conn = None
        try:
            if existing_conn is None:
                myconn = connection_factory.ConnectionFactory.create()
                conn = myconn.getconnection()
                is_new_connection = True
            else:
                conn = existing_conn
            return conn
        except:
            raise


    def save_excel_sheet_info_list(self, excel_sheet_info_list, existing_conn=None):
        conn = None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.get_excel_sheet_dao(conn)
            if excel_sheet_info_list is not None and len(excel_sheet_info_list) > 0:
                for excel_sheet_info in excel_sheet_info_list:
                    dao.insert_excel_sheet_data(excel_sheet_info)
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()

    def get_excel_sheet_info_list(self, start_limit, count, existing_conn=None):
        conn=None
        try:
            conn = self.get_connection(existing_conn)
            dao = dao_factory.DaoFactory.get_excel_sheet_dao(conn)
            excel_sheet_info_list = dao.get_excel_sheet_info_list(start_limit, count)
            return excel_sheet_info_list
        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()



    def save_info_from_xlrd(self, wb_path, existing_conn=None):
        conn = None
        wb = None
        try:
            print 'entered save_info_from_xlrd'
            excel_reader = excel_sheet_reader.ExcelReader()
            wb = open_workbook(wb_path)
            ##### Start reading excel sheet
            excel_sheet_info_list = excel_reader.read_company_info(wb)
            ###saving excel_sheet_info in db
            self.save_excel_sheet_info_list(excel_sheet_info_list, conn)
            print 'finished save_info_from_xlrd'

        except:
            raise
        finally:
            if existing_conn is None and conn is not None:
                conn.close()
            if wb is not None:
                wb.release_resources()
