% rebase('base.tpl')

<h1>Vislice ste obiskali že {{stevec}}-krat.</h1>

<blockquote>
Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa). <small>Študentje</small>
</blockquote>

<img src="img/10.jpg" alt="obesanje">

<form action="/igra/" method="post">
<button type="submit">Nova igra</button>
</form>
<form action="/pretekle_igre/" method="post">
<button type="submit">PRETEKLE IGRE</button>
</form>