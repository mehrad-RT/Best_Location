document.addEventListener("DOMContentLoaded", function() {
    const dataContainer = document.getElementById("dataContainer");

    const dataRows = [
        {district_number: 1, size: 110, product_grade: 'A', profit: '224.10%'},
        {district_number: 2, size: 32, product_grade: 'B', profit: '98.09%'},
        {district_number: 3, size: 150, product_grade: 'A', profit: '260.47%'},
        {district_number: 4, size: 250, product_grade: 'A', profit: '318.42%'},
        {district_number: 5, size: 230, product_grade: 'B', profit: '222.78%'},
        {district_number: 10, size: 53, product_grade: 'C', profit: '238.13%'},
        {district_number: 22, size: 300, product_grade: 'B', profit: '569.92%'},
    ];

    const classNames = ['one', 'two', 'three'];
    const rowElements = classNames.map(() => {
        const rowDiv = document.createElement('div');
        rowDiv.classList.add('row');
        dataContainer.appendChild(rowDiv);
        return rowDiv;
    });

    let currentIndex = 0;

    function createRowHtml(data) {
        return `District number: ${data.district_number} | Size: ${data.size} | Product grade: ${data.product_grade} | <span class="profit">Profit: ${data.profit}</span>`;
    }

    function updateRows() {
        rowElements.forEach((row, index) => {
            const dataIndex = (currentIndex + index) % dataRows.length;
            row.innerHTML = createRowHtml(dataRows[dataIndex]);
        });
    }

    function rotateRows() {
        rowElements.forEach((row, index) => {
            classNames.forEach(className => row.classList.remove(className));
            row.classList.add(classNames[index]);
        });

        setTimeout(() => {
            currentIndex++;
            updateRows();
        }, 500);
    }

    updateRows();
    setInterval(rotateRows, 3000);
});
