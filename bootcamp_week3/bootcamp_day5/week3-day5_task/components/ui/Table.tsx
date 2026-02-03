import React from 'react';

interface TableProps {
  data: { id: number; name: string; email: string }[];
}

const Table: React.FC<TableProps> = ({ data }) => {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white rounded shadow">
        <thead>
          <tr className="bg-gray-200 text-left">
            <th className="px-4 py-2">ID</th>
            <th className="px-4 py-2">Name</th>
            <th className="px-4 py-2">Email</th>
          </tr>
        </thead>
        <tbody>
          {data.map((user) => (
            <tr key={user.id} className="border-t">
              <td className="px-4 py-2">{user.id}</td>
              <td className="px-4 py-2">{user.name}</td>
              <td className="px-4 py-2">{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
