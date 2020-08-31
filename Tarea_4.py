import webbrowser
import os
import sys


lista =[]


def reporte():
    htmlfile = open("Reportes.html","w")
    htmlfile.write("""
<!DOCTYPE html>
<html>
<head>
    <meta charset = "utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">
    <title> Reporte </title>
</head>
<style type ="text/css">
h1{
    font-family:sans-serif;
    text-align: center;
}      

table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
th, td{
    padding:10px;
    }
th{
    font-family:sans-serif;
    text-align: left;
    }
table{
    background-color: rgba(108, 174, 35, 1);   
    }

thead{
    background-color: rgba(234, 52, 16, 1); 
    border-bottom: solid 5px #000000;
    color:white;
    }
</style>
<body>
        <h1>Reporte</h1>
        <table style= "width: 100%">
		<thead>
            <tr>
		        <th>
			        Nombre
			    </th>
			    <th>
    			    Edad
	    	    </th>
			    <th>
        			Activo
	    		</th>
		    	<th>
    			    Saldo
		        </th>
		    </tr>
        </thead>
""")

    for dato  in lista:
        datos = dato.split(',')
        htmlfile.write("        <tr>\n")
        htmlfile.write("            <td>")
        htmlfile.write(datos[0])
        htmlfile.write("</td>\n")
        htmlfile.write("            <td>")
        htmlfile.write(datos[1])
        htmlfile.write("</td>\n")
        htmlfile.write("            <td>")
        htmlfile.write(datos[2])
        htmlfile.write("</td>\n")
        htmlfile.write("            <td>")
        htmlfile.write(datos[3])
        htmlfile.write("</td>\n")
        htmlfile.write("        </tr>\n")
    htmlfile.write("</body>\n")
    htmlfile.write("</html>")
    htmlfile.close()
        



if __name__ == '__main__':
    lista.append("Made,564,True,")
    lista.append("Osmar,21,True,7000")
    lista.append("Analy,22,True,3000")  
    lista.append("Madelyn,16,True,5000")
    lista.append("Jason,24,True,4000")
    lista.append("Fernando,18,False,5000")
    lista.append("Norma,51,True,10000")
    lista.append("Daniel,27,True,6000")
    lista.append("Meyli,17,False,7000")
    lista.append("Valery,25,True,8000")
    reporte()
    webbrowser.open('Reportes.html')
     


