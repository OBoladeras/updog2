function searcherfunc() {
    searcher = document.querySelector('#tableData_filter input');
    let images = document.querySelectorAll('.image');
    for (let i = 0; i < images.length; i++) {
        let image = images[i];
        let filename = image.querySelector('p').textContent;
        if (filename.toLowerCase().includes(searcher.value.toLowerCase())) {
            image.style.display = 'block';
        } else {
            image.style.display = 'none';
        }
    }
}

function downloadAll() {
    for (let i = 0; i < fileNames.length; i++) {
        const link = document.createElement('a');
        link.href = `/images/download/${fileNames[i]}`;
        link.download = fileNames[i];
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}