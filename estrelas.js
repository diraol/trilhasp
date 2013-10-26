var saveAvaliacao = function (id) {
    var callee = id.toString();
    var botao = document.getElementById(id);
    var indiceAvaliacao = botao.parentNode.parentNode.id.slice(-1); 
    var indiceStar = id.charAt(5);
    var span = document.getElementById('star-' + indiceStar + '-span-avaliacao-' + indiceAvaliacao);
    
    coloreEstrelasAnteriores (indiceStar, span, indiceAvaliacao);
    descoloreEstrelasPosteriores (indiceStar, span, indiceAvaliacao);
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

