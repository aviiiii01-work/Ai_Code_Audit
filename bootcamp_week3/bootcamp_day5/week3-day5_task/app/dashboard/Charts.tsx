'use client';

import React from 'react';

const Charts: React.FC = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {/* Example chart cards */}
      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-bold mb-2">Sales Chart</h2>
        <div className="h-40 bg-gray-200 flex items-center justify-center">
          Chart Placeholder
        </div>
      </div>

      <div className="bg-white p-4 rounded shadow">
        <h2 className="text-lg font-bold mb-2">Revenue Chart</h2>
        <div className="h-40 bg-gray-200 flex items-center justify-center">
          Chart Placeholder
        </div>
      </div>
    </div>
  );
};

export default Charts;
