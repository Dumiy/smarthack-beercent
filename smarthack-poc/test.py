import pyodbc

driver="{SQL Server Native Client 11.0}"
server="smarthack2020server.database.windows.net"
database="Smarthack2020SearchDB"
username="beercent"
Pwd="Password01!"
print('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+Pwd)

pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+Pwd+";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")


with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+Pwd+";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * from [Smarthack2020SearchDB].[dbo].[review_db]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()