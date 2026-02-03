"use client";

import { usePathname } from "next/navigation";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";

export default function DashboardLayout({ children }) {
  const pathname = usePathname();

  // navbar only on /dashboard
  const showNavbar = pathname === "/dashboard";

  return (
    <div className="flex">
      <Sidebar />

      <main className="flex-1">
        {showNavbar && <Navbar />}
        {children}
      </main>
    </div>
  );
}
