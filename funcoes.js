var saveAvaliacao = function (id) {
    var callee = id.toString();
    var botao = document.getElementById(id);
    var indiceAvaliacao = botao.parentNode.parentNode.id.slice(-1); 
    var indiceStar = id.charAt(5);
    var span = document.getElementById('star-' + indiceStar + '-span-avaliacao-' + indiceAvaliacao);
    
    coloreEstrelasAnteriores (indiceStar, span, indiceAvaliacao);
    descoloreEstrelasPosteriores (indiceStar, span, indiceAvaliacao);

    enableSalvarOuContinuar();
}

var coloreEstrelasAnteriores = function (indiceStar, span, indiceAvaliacao) {
    span.className = "glyphicon glyphicon-star";
    if (indiceStar > '1'){
	var nextIndiceStar = indiceStar - 1;
	var nextSpan = document.getElementById('star-' + nextIndiceStar + '-span-avaliacao-' + indiceAvaliacao);
	
	coloreEstrelasAnteriores(nextIndiceStar, nextSpan, indiceAvaliacao);
    }
}

var descoloreEstrelasPosteriores = function(indiceStar, span, indiceAvaliacao) {
    if (indiceStar < '5') {
	var nextIndiceStar = parseInt(indiceStar,10) + 1;
	var nextSpan = document.getElementById('star-' + nextIndiceStar + '-span-avaliacao-' + indiceAvaliacao);
	nextSpan.className = "glyphicon glyphicon-star-empty";
	
	descoloreEstrelasPosteriores(nextIndiceStar, nextSpan, indiceAvaliacao);
    }
}

var enableSalvarOuContinuar = function() {
    var botaoSalvar = document.getElementById('salvar');
    var botaoContinuar = document.getElementById('continuar');
    if (botaoSalvar !== null) 
	botaoSalvar.className = "btn btn-lg btn-primary btn-block";
    else if (botaoContinuar !== null)
	botaoContinuar.className = "btn btn-lg btn-primary btn-block";
}

var getNotaAvaliacao = function(idAvaliacao) {
    var estrelasSelecionadas  = document.getElementById('avaliacao-' + idAvaliacao).getElementsByClassName('glyphicon-star');
    var size = estrelasSelecionadas.length;
    var ultimaEstrelaSelecionada = estrelasSelecionadas.item(size-1);
    return (ultimaEstrelaSelecionada  === null)? 0 : ultimaEstrelaSelecionada.id.charAt(5);  ultimaEstrelaSelecionada = document.getElementById('avaliacao-' + idAvaliacao).getElementsByClassName('glyphicon-star').item(this.length-1);
}