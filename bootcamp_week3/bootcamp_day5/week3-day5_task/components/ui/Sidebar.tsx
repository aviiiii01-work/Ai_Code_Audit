import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 h-auto bg-gray-900 text-gray-200 p-6 space-y-6">
      <h1 className="text-xl font-bold">Start Bootstrap</h1>

      <nav className="space-y-4">
        <div className="text-gray-400 uppercase text-xs">Core</div>

        <Link href="/dashboard" className="block p-2 rounded bg-gray-800">
          Dashboard
        </Link>

        <div className="text-gray-400 uppercase text-xs">Pages</div>

        <Link href="/dashboard/users" className="block p-2 hover:bg-gray-800 rounded">
          Users Table
        </Link>

        <Link href="/dashboard/profile" className="block p-2 hover:bg-gray-800 rounded">
          Profile
        </Link>
      </nav>
    </aside>
  );
}
