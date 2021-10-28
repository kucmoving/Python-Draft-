#function: https://developers.google.com/sheets/api/reference/rest
#get value閱讀
to_get = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="test!A1:B4").execute()
values = result.get('values', []) #取純粹表內內容

#update value更新
aoa = [["yes,no"],[12331,3131]]
to_update = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                           range="A1:B4", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()  ###不如予位置就會自動產生(A1:B4最後的位)
                            ###開新table要用service, 不可以在此增加

#append 新增一行
data = [["yesyes", "nono", "gg"],["bobo","no","cancel"]]
to_append = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="jes!A1:G1", valueInputOption="USER_ENTERED",
                            insertDataOption="INSERT_ROWS", body={"values":data}).execute()  #body={'majorDimension' : 'ROWS', 'value': values}

#刪除clear (但format不會刪去)
to_clear = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="jes!A1:B3").execute()

###csv匯入
file = r'................'
df = pd.read_csv(file)
df.replace(np.nan, '', inplace=True)





