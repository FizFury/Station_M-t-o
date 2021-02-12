
// const data = $.get(
//     "192.168.8.248:5001/print_10last_data"
// );
// console.log(data);
let temperatureList = [];
let humidityList = [];

(async function (){

  let apiData = await $.get("http://192.168.8.248:5000/print_graph_data");
  apiData = apiData.responseJSON;

  let temperatureList = [];
  let humiditylist = [];

  function tempAndHumidityUpdate(data){
    for(const [i, donnee] of Object.entries(data)) {
      // humiditylist.push([donnee.date, donnee.humidity]);
      temperatureList.push([parseInt(i), donnee.temperature]);

    }
  }

  tempAndHumidityUpdate(apiData);

  console.log(temperatureList);
  console.log(humiditylist);



})()


document.addEventListener('DOMContentLoaded', function () {
  const chart = Highcharts.chart('container', {
    chart: {
      type: 'line'
    },
    title: {
      text: 'Graphique'
    },
    subtitle: {
      text: 'Source: WorldClimate.com'
    },
    yAxis: {
      labels : {
        format: '{value}'
      },
      title: {
        text: 'Temperature (°C)'
      }
    },
    plotOptions: {
      line: {
        dataLabels: {
          enabled: true
        },
        enableMouseTracking: false
      }
    },
    series: [{
      name: 'Température',
      data: temperatureList
    }]
  });
  });