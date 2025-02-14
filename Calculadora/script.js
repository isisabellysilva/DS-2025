function adicionarAoDisplay(valor) {
    const display = document.getElementById('display');
    display.value += valor;
}

function limparDisplay() {
    const display = document.getElementById('display');
    display.value = '';
}

function calcularResultado() {
    const display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Erro';
    }
}