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

// fourth question
const economy = () => {
  fetch("http://localhost:8000/api/fourth")
    .then(response => response.json())
    .then(res => drawEconomy(res["bowlers"], res["economy"]));
};

const drawEconomy = (bowlers, economy) => {
  var chart = Highcharts.chart("container", {
    title: {
      text: "Economical Bowlers"
    },
    subtitle: {
      text: "IPL Data"
    },
    xAxis: {
      title: {
        text: "Bowler"
      },
      categories: bowlers
    },
    yAxis: {
      title: {
        text: "Economy"
      }
    },
    series: [
      {
        type: "column",
        name: "Teams",
        colorByPoint: true,
        data: economy,
        showInLegend: false
      }
    ]
  });
};

const sixes = () => {
  fetch("http://localhost:8000/api/fifth")
    .then(response => response.json())
    .then(res => drawSixes(res["batsman"], res["sixes"]));
};

const drawSixes = (batsman, sixes) => {
  var chart = Highcharts.chart("container", {
    title: {
      text: "Sixes in IPL 2016"
    },
    subtitle: {
      text: "IPL Data"
    },
    xAxis: {
      title: {
        text: "Batsman"
      },
      categories: batsman
    },
    yAxis: {
      title: {
        text: "Sixes"
      }
    },
    series: [
      {
        type: "column",
        name: "Teams",
        colorByPoint: true,
        data: sixes,
        showInLegend: false
      }
    ]
  });
};
