const matchesPlayed = () => {
  fetch("http://localhost:8000/api/first")
    .then(response => response.json())
    .then(res => drawChart(res["season"], res["matches"]));
};
const drawChart = (seasons, matches) => {
  console.log(seasons, matches);
  var chart = Highcharts.chart("container", {
    title: {
      text: "Matches played"
    },
    subtitle: {
      text: "IPL Data"
    },
    xAxis: {
      title: {
        text: "Seasons"
      },
      categories: seasons
    },
    yAxis: {
      title: {
        text: "Match played"
      }
    },
    series: [
      {
        type: "column",
        name: "Matches",
        colorByPoint: true,
        data: matches,
        showInLegend: false
      }
    ]
  });
};

// matches won by teams per season
const matchesWon = () => {
  fetch("http://localhost:8000/api/second")
    .then(response => response.json())
    .then(res => drawData(res["years"], res["seriesdata"]));
};

const drawData = (years, seriesdata) => {
  console.log(years, seriesdata);
  Highcharts.chart("container", {
    chart: {
      type: "column"
    },
    title: {
      text: "Matches won per team"
    },
    xAxis: {
      categories: years,
      title: {
        text: "Teams"
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: "Matches won"
      }
    },
    legend: {
      reversed: true
    },
    plotOptions: {
      series: {
        stacking: "normal"
      }
    },
    series: seriesdata
  });
};

const extraRuns = () => {
  fetch("http://localhost:8000/api/third")
    .then(response => response.json())
    .then(res => drawExtras(res["teams"], res["extras"]));
};
const drawExtras = (teams, extras) => {
  console.log(teams, extras);
  var chart = Highcharts.chart("container", {
    title: {
      text: "Extra runs"
    },
    subtitle: {
      text: "IPL Data"
    },
    xAxis: {
      title: {
        text: "Teams"
      },
      categories: teams
    },
    yAxis: {
      title: {
        text: "Extra runs"
      }
    },
    series: [
      {
        type: "column",
        name: "Teams",
        colorByPoint: true,
        data: extras,
        showInLegend: false
      }
    ]
  });
};