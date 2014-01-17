<html>
	<head>
	</head>
	
	
	<body>
		<h1>Pagina HOME SERGI</h1>
		MISSATGE: ${missatge}<br />
		Llista de nombres:<br />
		
		% for num in nombres:
			${num}<br />
		% endfor
	</body>
</html>
