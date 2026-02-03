"use client";

import Link from "next/link";
import Button from "@/components/ui/Button";

export default function HomePage() {
  return (
    <div className="min-h-screen w-full bg-gray-100 flex flex-col items-center p-8">

      {/* Hero Section */}
      <div className="max-w-3xl text-center mt-12">
        <h1 className="text-5xl font-extrabold text-gray-900 drop-shadow-sm">
          Welcome to Your Dashboard System
        </h1>

        <p className="mt-4 text-lg text-gray-600 leading-relaxed">
          A simple and powerful interface to manage your users, view stats, customize your profile
          and explore advanced admin tools — all in one place.
        </p>

        <div className="mt-8 flex justify-center gap-4">
          <Link href="/login">
            <Button className="h-12 px-8 text-lg rounded-xl">Login</Button>
          </Link>

          <Link href="/dashboard">
            <Button variant="outline" className="h-12 px-8 text-lg rounded-xl">
              Enter Dashboard
            </Button>
          </Link>
        </div>
      </div>

      {/* Feature Section */}
      <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl w-full">

        <div className="bg-white shadow-md p-6 rounded-2xl border border-gray-200">
          <h2 className="text-xl font-bold text-gray-900 mb-2">User Management</h2>
          <p className="text-gray-600">
            View, filter, and manage user data with clean table UI and modern interactions.
          </p>
        </div>

        <div className="bg-white shadow-md p-6 rounded-2xl border border-gray-200">
          <h2 className="text-xl font-bold text-gray-900 mb-2">Profile Controls</h2>
          <p className="text-gray-600">
            Update your profile, manage credentials, and personalize your experience.
          </p>
        </div>

        <div className="bg-white shadow-md p-6 rounded-2xl border border-gray-200">
          <h2 className="text-xl font-bold text-gray-900 mb-2">Live Dashboard</h2>
          <p className="text-gray-600">
            Visualize your data using charts, insights, and real-time UI elements.
          </p>
        </div>
      </div>

      {/* Footer */}
      <div className="mt-20 text-gray-500 text-sm">
        © {new Date().getFullYear()} Bootcamp Dashboard — All Rights Reserved.
      </div>
    </div>
  );
}
