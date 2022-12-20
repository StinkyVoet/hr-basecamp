import 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js'
import 'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'


Chart.defaults.color = 'white'
Chart.defaults.elements.line.borderWidth = 1;

const canvas = document.querySelector('#temperature_chart')

const labels = JSON.parse(canvas.dataset.labels.replaceAll('\'', '"'))
const temperatures = JSON.parse(canvas.dataset.temperatures.replaceAll('\'', '"'))
const humidity = JSON.parse(canvas.dataset.humidity.replaceAll('\'', '"'))
const pressure = JSON.parse(canvas.dataset.pressure.replaceAll('\'', '"'))

delete canvas.dataset.labels
delete canvas.dataset.temperatures
delete canvas.dataset.humidity
delete canvas.dataset.pressure

const chart = new Chart(canvas, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                data: temperatures,
                label: "Temperature (°C)",
                backgroundColor: 'red',
                borderColor: 'red',
                yAxisID: 'y',
            },
            {
                data: humidity,
                label: "Humidity",
                backgroundColor: 'blue',
                borderColor: 'blue',
                yAxisID: 'y',
            },
            {
                data: pressure,
                label: "Pressure",
                backgroundColor: 'yellow',
                borderColor: 'yellow',
                yAxisID: 'y1',
            },
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',
            },
        },
    }
})

setInterval(async function () {
    await axios.get('/data')
        .then((response) => {
            chart.data.labels = response.data.labels
            chart.data.datasets[0].data = response.data.temperatures
            chart.data.datasets[1].data = response.data.humidity
            chart.data.datasets[2].data = response.data.pressure

            chart.update()

            document.querySelectorAll('.statistic').forEach((e) => {
                e.textContent = response.data.statistics[e.dataset.statistic][e.dataset.value]
            })
        })
}, 10000)
