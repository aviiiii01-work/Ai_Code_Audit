"use client";

import { useState } from "react";

const mockUsers = [
  { name: "User", email: "user@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Dr. Ray Stoltenberg", email: "rosalinda42@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Mrs. Mertie Murray MD", email: "ernser.susanna@example.net", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Gilbert Rice", email: "willard.walter@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Sydnie Rau", email: "doug.padberg@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Mr. Arvid Veum DDS", email: "schinner.meaghan@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Jayme Beier DDS", email: "orn.ahmed@example.com", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
  { name: "Uriah Swaniawski", email: "wilburn.champlin@example.org", role: "User", created: "18/10/2024 05:27", updated: "18/10/2024 05:27" },
];

export default function UsersPage() {
  const [search, setSearch] = useState("");

  const filtered = mockUsers.filter((u) =>
    u.name.toLowerCase().includes(search.toLowerCase()) ||
    u.email.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="w-full min-h-screen bg-gray-100 flex justify-center py-10">
      <div className="w-[1100px] bg-white rounded-2xl shadow p-8 border">

        <h2 className="text-2xl font-bold mb-4 text-gray-900">Users</h2>

        <div className="flex justify-end mb-4 text-gray-300">
          <input
            className="border-2 p-2 rounded-lg w-60 text-gray-900"
            placeholder="Search"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        {/* Table */}
        <table className="w-full text-left border-collapse">
          <thead className="bg-gray-100 text-gray-900">
            <tr>
              <th className="p-3">Name</th>
              <th className="p-3">Email</th>
              <th className="p-3">Role</th>
              <th className="p-3">Created At</th>
              <th className="p-3">Updated At</th>
            </tr>
          </thead>

          <tbody className ="text-gray-900">
            {filtered.map((u, i) => (
              <tr key={i} className="border-b hover:bg-gray-50">
                <td className="p-3">{u.name}</td>
                <td className="p-3">{u.email}</td>
                <td className="p-3">{u.role}</td>
                <td className="p-3">{u.created}</td>
                <td className="p-3">{u.updated}</td>
              </tr>
            ))}
          </tbody>
        </table>

      </div>
    </div>
  );
}
