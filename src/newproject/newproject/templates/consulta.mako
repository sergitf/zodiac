<h1>Introduiex el teu signe</h1>

<form method="post">

	<select id="select1" name="select1">
	   <option value = "0">Selecciona</option>
	   <option value = "1">1</option>
	   <option value = "2">2</option>
	   <option value = "3">3</option>
	   <option value = "4">4</option>
	   <option value = "5">5</option>
	   <option value = "6">6</option>
	   <option value = "7">7</option>
	   <option value = "8">8</option>
	   <option value = "9">9</option>
	   <option value = "10">10</option>
	   <option value = "11">11</option>
	   <option value = "12">12</option>
	   <option value = "13">13</option>
	   <option value = "14">14</option>
	   <option value = "15">15</option>
	   <option value = "16">16</option>
	   <option value = "17">17</option>
	   <option value = "18">18</option>
	   <option value = "19">19</option>
	   <option value = "20">20</option>
	   <option value = "21">21</option>
	   <option value = "22">22</option>
	   <option value = "23">23</option>
	   <option value = "24">24</option>
	   <option value = "25">25</option>
	   <option value = "26">26</option>
	   <option value = "27">27</option>
	   <option value = "28">28</option>
	   <option value = "29">29</option>
	   <option value = "30">30</option>
	   <option value = "31">31</option>

	</select>

	<select id="select2" name="select2">
	   <option value = "0">Selecciona</option>
	   <option value = "1">Gener</option>
	   <option value = "2">Febrer</option>
	   <option value = "3">Març</option>
	   <option value = "4">Abril</option>
	   <option value = "5">Maig</option>
	   <option value = "6">Juny</option>
	   <option value = "7">Juliol</option>
	   <option value = "8">Agost</option>
	   <option value = "9">Setembre</option>
	   <option value = "10">Octubre</option>
	   <option value = "11">Novembre</option>
	   <option value = "12">Decembre</option>
	</select>

	<input type="text" name="any" value="YYYY" />

	<input type="submit" value="Consultar" />
</form>

% if dia:
	<p>Dia: ${dia}</p>
	<p>Mes: ${mes}</p>
	<p>Missatge: ${missatge}</p>
	<p>Signe: ${zodiac}</p>
	<img src="static/fotos/${zodiac}.png" />

% endif
