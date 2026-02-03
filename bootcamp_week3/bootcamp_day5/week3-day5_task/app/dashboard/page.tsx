"use client";

import { useState, useMemo, useEffect } from "react";
import dynamic from "next/dynamic";
import Link from "next/link";
import "@/components/charts/charts-setup";

import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Input from "@/components/ui/Input";
import Badge from "@/components/ui/Badge";
import Modal from "@/components/ui/Modal";

// Dynamic charts
const AreaChart = dynamic(() => import("@/components/ui/AreaChart"), { ssr: false });
const BarChart = dynamic(() => import("@/components/ui/BarChart"), { ssr: false });

// Debounce hook
function useDebounce(value: string, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}

export default function Dashboard() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const debouncedSearch = useDebounce(search, 250);

  // Demo cards
  const cards = useMemo(
    () => [
      { id: 1, title: "Primary Card", body: "Some quick info", color: "blue", badge: "New" },
      { id: 2, title: "Warning Card", body: "Important notice", color: "yellow", badge: "Info" },
      { id: 3, title: "Success Card", body: "All good", color: "green", badge: "OK" },
      { id: 4, title: "Danger Card", body: "Requires attention", color: "red", badge: "Alert" },
    ],
    []
  );

  const filteredCards = useMemo(() => {
    const q = debouncedSearch.trim().toLowerCase();
    if (!q) return cards;
    return cards.filter(
      (c) => c.title.toLowerCase().includes(q) || c.body.toLowerCase().includes(q)
    );
  }, [cards, debouncedSearch]);

  // Chart loading delay
  const [chartsReady, setChartsReady] = useState(false);
  useEffect(() => {
    const timer = setTimeout(() => setChartsReady(true), 400);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="w-full min-h-screen bg-gray-50 p-6 flex flex-col gap-6">

      {/* Header */}
      <h1 className="text-3xl font-bold text-gray-800">Dashboard</h1>

      {/* Navigation Buttons (Final Correct Version) */}
      <div className="flex gap-4">
        <Link href="/dashboard">
          <Button>Dashboard</Button>
        </Link>

        <Link href="/dashboard/profile">
          <Button>Profile</Button>
        </Link>

        <Link href="/dashboard/users">
          <Button>Users</Button>
        </Link>
      </div>

      {/* Search Bar */}
      <div className="max-w-xl">
        <Card>
          <div className="flex gap-3 items-center">
            <Input
              placeholder="Search dashboard cards..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
            <Button onClick={() => setOpen(true)} className="whitespace-nowrap">
              Quick Search
            </Button>
          </div>
        </Card>
      </div>

      {/* Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {filteredCards.map((c) => (
          <Card key={c.id} className="p-0">
            <div
              className={`p-4 rounded-t-lg text-white ${
                c.color === "blue"
                  ? "bg-blue-600"
                  : c.color === "green"
                  ? "bg-green-600"
                  : c.color === "red"
                  ? "bg-red-600"
                  : "bg-yellow-400"
              }`}
            >
              <div className="flex justify-between items-start">
                <div>
                  <h2 className="font-bold text-lg">{c.title}</h2>
                  <p className="mt-2 text-sm">{c.body}</p>
                </div>
                <Badge color={c.color}>{c.badge}</Badge>
              </div>

              <div className="mt-4">
                <Button
                  variant="outline"
                  className="bg-white text-current border-white hover:bg-white/90"
                  onClick={() => setOpen(true)}
                >
                  View Details
                </Button>
              </div>
            </div>
          </Card>
        ))}
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <Card>
          <h2 className="text-lg font-semibold text-gray-700 mb-3">Area Chart Example</h2>
          <div className="w-full h-64 bg-white border rounded-lg p-3">
            {!chartsReady ? (
              <div className="w-full h-full flex items-center justify-center text-gray-400">
                Loading chart…
              </div>
            ) : (
              <AreaChart />
            )}
          </div>
        </Card>

        <Card>
          <h2 className="text-lg font-semibold text-gray-700 mb-3">Bar Chart Example</h2>
          <div className="w-full h-64 bg-white border rounded-lg p-3">
            {!chartsReady ? (
              <div className="w-full h-full flex items-center justify-center text-gray-400">
                Loading chart…
              </div>
            ) : (
              <BarChart />
            )}
          </div>
        </Card>
      </div>

      {/* Modal */}
      <Modal open={open} onClose={() => setOpen(false)} title="Card Details">
        <p className="text-gray-700">This is placeholder modal content.</p>
      </Modal>
    </div>
  );
}
