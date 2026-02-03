"use client";

import {
  Chart,
  LineElement,
  BarElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
  Tooltip,
  Legend
} from "chart.js";

Chart.register(
  LineElement,
  BarElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Filler,
  Tooltip,
  Legend
);
