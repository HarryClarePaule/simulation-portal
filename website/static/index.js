function deleteNote(id) {
    fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ id: id}),
    }).then((_res)=> {
    window.location.href = "/HPCtable";
    });
}