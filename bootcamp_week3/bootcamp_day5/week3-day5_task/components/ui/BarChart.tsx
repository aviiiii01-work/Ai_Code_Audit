"use client";

import { Bar } from "react-chartjs-2";

export default function BarChart() {
  const data = {
    labels: ["Python", "Java", "C++", "JavaScript", "DSA"],
    datasets: [
      {
        label: "Course Progress (%)",
        data: [85, 70, 60, 90, 75],
        backgroundColor: "rgba(54, 162, 235, 0.6)",
        borderColor: "rgb(54, 162, 235)",
        borderWidth: 1,
      },
    ],
  };

  return <Bar data={data} />;
}
