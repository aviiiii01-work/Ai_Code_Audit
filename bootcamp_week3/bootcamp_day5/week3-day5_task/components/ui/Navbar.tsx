"use client";
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full h-14 bg-gray-900 text-white flex items-center justify-between px-6">
      <h2 className="text-xl font-bold">Dashboard</h2>

      <Link
        href="/profile"
        className="px-4 py-2 bg-white text-black rounded-md font-semibold"
      >
        Profile
      </Link>
    </nav>
  );
}
