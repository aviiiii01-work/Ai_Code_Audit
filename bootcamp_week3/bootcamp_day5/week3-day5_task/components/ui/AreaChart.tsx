"use client";

import { Line } from "react-chartjs-2";

export default function AreaChart() {
  const data = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May"],
    datasets: [
      {
        label: "Users",
        data: [10, 40, 20, 60, 30],
        fill: true,
        borderWidth: 2,
      },
    ],
  };

  return <Line data={data} />;
}
