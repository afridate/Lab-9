document.getElementById('add-button').addEventListener('click', () => {
    const steps = document.getElementById('steps-input').value;
    const date = document.getElementById('date-input').value;

    if (!steps || !date) {
        alert('Заполните оба поля: количество шагов и дату');
        return;
    }

    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ steps: parseInt(steps), date: date })
    })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Не удалось добавить запись');
            }
        });
});

document.getElementById('clear-button').addEventListener('click', () => {
    fetch('/clear', { method: 'POST' })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Не удалось очистить ленту');
            }
        });
});
